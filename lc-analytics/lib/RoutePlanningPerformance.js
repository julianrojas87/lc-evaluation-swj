import config from '../config.js';
import fs from 'fs';
import PlannerJS from 'plannerjs';

export async function runBenchmark(source, querySet, test, cycles) {
    if (!fs.existsSync(`${config.rootPath}/results/${source}`)) fs.mkdirSync(`${config.rootPath}/results/${source}`);
    const results = [];
    let scannedCxs = 0;
    let pagesFetched = 0;
    let bytesTransferred = 0;

    console.log(`Starting evaluation for ${source}`);
    const planner = new PlannerJS.FlexibleTransitPlanner();
    const { EventBus, EventType } = PlannerJS;

    EventBus.on(EventType.ConnectionScan, () => { scannedCxs++ });
    EventBus.on(EventType.ResourceFetch, r => {
        if (r.datatype) {
            pagesFetched++;
            bytesTransferred += r.size;
        }
    });

    planner.addConnectionSource(`${config.lcServer}/${source}/connections`);
    planner.addStopSource(`${config.lcServer}/${source}/stops`);

    for (let i = 0; i < cycles; i++) {
        for (let j = 0; j < querySet.length; j++) {
            scannedCxs = 0;
            pagesFetched = 0;
            bytesTransferred = 0;


            console.log(`Round ${i} - Executing query from ${querySet[j].from} to ${querySet[j].to}`);

            const t0 = new Date();
            const route = await runQuery(planner, {
                from: querySet[j].from,
                to: querySet[j].to,
                minimumDepartureTime: new Date(querySet[j].minimumDepartureTime),
                maximumArrivalTime: new Date(querySet[j].maximumArrivalTime)
            });
            const responseTime = new Date() - t0;
            console.log(`\tresponse time = ${responseTime} ms`);

            if (results[j]) {
                results[j].responseTime += responseTime;
            } else {
                results[j] = {
                    query: querySet[j],
                    route: route,
                    responseTime: responseTime,
                    scannedConnections: scannedCxs,
                    pagesFetched: pagesFetched,
                    bytesTransferred: bytesTransferred
                };
            }
            console.log('*********************************************************');
        }
    }

    // Calculate averages
    let totalAverageResponseTime = 0;
    results.forEach(r => {
        r.responseTime = r.responseTime / cycles;
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

    fs.writeFileSync(`${config.rootPath}/results/${source}/results_${test}.json`,
        JSON.stringify({
            averageResponseTime: totalAverageResponseTime,
            p10: results[p10].responseTime,
            p50: results[p50].responseTime,
            p75: results[p75].responseTime,
            p90: results[p90].responseTime,
            results: results
        }, null, 3), 'utf8');
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