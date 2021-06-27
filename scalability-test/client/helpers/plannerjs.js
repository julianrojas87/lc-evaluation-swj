const { parentPort, workerData } = require("worker_threads");
const PlannerJS = require('plannerjs');

async function run() {
    console.log(`Starting Planner.js evaluation for ${workerData.operator}`);
    const results = [];
    const planner = new PlannerJS.FlexibleTransitPlanner();
    const { EventBus, EventType } = PlannerJS;

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
    await runQuery(planner, {
        from: querySet[0].from,
        to: querySet[0].to,
        minimumDepartureTime: new Date(querySet[0].minimumDepartureTime),
        maximumArrivalTime: new Date(querySet[0].maximumArrivalTime)
    });

    for (let i = 0; i < workerData.cycles; i++) {
        for (let j = 0; j < querySet.length; j++) {
            scannedCxs = 0;
            pagesFetched = 0;
            bytesTransferred = 0;

            //console.log(`Round ${i} - Executing query from ${querySet[j].from} to ${querySet[j].to}`);

            const t0 = new Date();
            const route = await runQuery(planner, {
                from: querySet[j].from,
                to: querySet[j].to,
                minimumDepartureTime: new Date(querySet[j].minimumDepartureTime),
                maximumArrivalTime: new Date(querySet[j].maximumArrivalTime)
            });
            const responseTime = new Date() - t0;
            //console.log(`\tresponse time = ${responseTime} ms`);

            if (responseTime > 10000) {
                timeouts++;
            }

            if (results[j]) {
                if (responseTime <= 10000) {
                    results[j].responseTime += responseTime;
                }
            } else {
                if (responseTime <= 10000) {
                    results[j] = {
                        query: querySet[j],
                        route: route,
                        responseTime: responseTime,
                        scannedConnections: scannedCxs,
                        pagesFetched: pagesFetched,
                        bytesTransferred: bytesTransferred
                    };
                }
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
    totalAverageResponseTime = totalAverageResponseTime / results.length;

    // Order by response time to calculate percentiles
    results.sort((a, b) => {
        return a.responseTime - b.responseTime;
    });

    // Calculate percentiles
    const p10 = Math.round(results.length * 0.1);
    const p50 = Math.round(results.length * 0.5);
    const p75 = Math.round(results.length * 0.75);
    const p90 = Math.round(results.length * 0.9);

    parentPort.postMessage({
        averageResponseTime: totalAverageResponseTime,
        timeouts,
        p10: results[p10].responseTime,
        p50: results[p50].responseTime,
        p75: results[p75].responseTime,
        p90: results[p90].responseTime,
    });
}

function runQuery(planner, q) {
    return new Promise((resolve, reject) => {
        planner
            .query(q)
            .on('data', path => {
                resolve(path);
            });
    });
}

run();
