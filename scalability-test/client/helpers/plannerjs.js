const { parentPort, workerData } = require("worker_threads");
const PlannerJS = require('plannerjs');
const { EventBus, EventType } = PlannerJS;

async function run() {
    console.log(`Starting Planner.js evaluation for ${workerData.operator}`);
    const results = new Map();
    const planner = new PlannerJS.FlexibleTransitPlanner();

    var scannedCxs = 0;
    var pagesFetched = 0;
    var bytesTransferred = 0;
    var timeouts = 0;

    EventBus.on(EventType.ConnectionScan, () => { scannedCxs++ });
    EventBus.on(EventType.ResourceFetch, r => {
        if (r.datatype) {
            pagesFetched++;
            bytesTransferred += r.size;
        }
    });

    planner.addConnectionSource(`${workerData.server}/${workerData.operator}/connections`);
    planner.addStopSource(`${workerData.server}/${workerData.operator}/stops`);

    const querySet = workerData.querySet

    // Do a warm up query so Planner.js fetches stops
    //console.log('Running warm up query');
    await runQuery(planner, {
        from: querySet[0].from,
        to: querySet[0].to,
        minimumDepartureTime: new Date(querySet[0].minimumDepartureTime),
        maximumArrivalTime: new Date(querySet[0].maximumArrivalTime),
        minimized: true
    }, false);


    for (let i = 0; i < workerData.cycles; i++) {
        for (let j = 0; j < querySet.length; j++) {
            scannedCxs = 0;
            pagesFetched = 0;
            bytesTransferred = 0;

            console.log(`Round ${i} - Executing query from ${querySet[j].from} to ${querySet[j].to} at ${querySet[j].minimumDepartureTime}`);

            const t0 = new Date();

            try {
                const minimumDepartureTime = new Date(querySet[j].minimumDepartureTime);
                let mementoDate = null;

                if(workerData.memento) {
                    mementoDate = new Date(minimumDepartureTime.getTime() - (3600 * 1000));
                }

                const route = await runQuery(planner, {
                    from: querySet[j].from,
                    to: querySet[j].to,
                    minimumDepartureTime,
                    maximumArrivalTime: new Date(querySet[j].maximumArrivalTime),
                    mementoDate
                }, false);
                const responseTime = new Date() - t0;
                //console.log(`\tresponse time = ${responseTime} ms`);

                if (results.has(j)) {
                    results.get(j).responseTime += responseTime;
                } else {
                    results.set(j, {
                        query: querySet[j],
                        route: route,
                        responseTime: responseTime,
                        scannedConnections: scannedCxs,
                        pagesFetched: pagesFetched,
                        bytesTransferred: bytesTransferred
                    });
                }
            } catch (err) {
                //console.log('\tquery timed out!');
                timeouts++;
            }
            //console.log('*********************************************************');
        }
    }

    // Calculate averages
    let totalAverageResponseTime = 0;
    results.forEach(r => {
        r.responseTime = r.responseTime / workerData.cycles;
        totalAverageResponseTime += r.responseTime;
        r.timePerConnection = r.responseTime / r.scannedConnections;
    });
    totalAverageResponseTime = totalAverageResponseTime / results.size;

    // Order by response time to calculate percentiles
    const sortedRes = Array.from(results.values());
    sortedRes.sort((a, b) => {
        return a.responseTime - b.responseTime;
    });

    // Calculate percentiles
    const p10 = Math.round(sortedRes.length * 0.1);
    const p50 = Math.round(sortedRes.length * 0.5);
    const p75 = Math.round(sortedRes.length * 0.75);
    const p90 = Math.round(sortedRes.length * 0.9);

    parentPort.postMessage({
        averageResponseTime: totalAverageResponseTime,
        timeouts,
        p10: sortedRes[p10] ? sortedRes[p10].responseTime : 0,
        p50: sortedRes[p50] ? sortedRes[p50].responseTime : 0,
        p75: sortedRes[p75] ? sortedRes[p75].responseTime : 0,
        p90: sortedRes[p90] ? sortedRes[p90].responseTime : 0,
    });
}

function runQuery(planner, q, timeout = true) {
    return new Promise((resolve, reject) => {
        let limit = null;
        const queryJob = planner.query(q);
        if (timeout) {
            limit = setTimeout(async () => {
                EventBus.emit(EventType.AbortQuery);
                reject();
            }, 10000);
        }

        queryJob.on('data', path => {
            if (limit) clearTimeout(limit);
            resolve(path);
        });
    });
}

run();
