import config from '../config.js';
import fs from 'fs';
import PlannerJS from 'plannerjs';

export async function runBenchmark(source, querySet, test, cycles) {
    if (!fs.existsSync(`${config.rootPath}/results/${source}`)) fs.mkdirSync(`${config.rootPath}/results/${source}`);
    const results = [];

    console.log(`Starting evaluation for ${source}`);
    const planner = new PlannerJS.FlexibleTransitPlanner();
    planner.addConnectionSource(`${config.lcServer}/${source}/connections`);
    planner.addStopSource(`${config.lcServer}/${source}/stops`);

    for (let i = 0; i < cycles; i++) {
        for (let j = 0; j < querySet.length; j++) {

            const firstLeg = querySet[j].legs[0];
            const lastLeg = querySet[j].legs[querySet[j].legs.length - 1];

            const query = {
                from: firstLeg.steps[0].startLocation.id,
                to: lastLeg.steps[lastLeg.steps.length - 1].stopLocation.id,
                minimumDepartureTime: new Date(firstLeg.steps[0].startTime)
            }

            console.log(`Round ${i} - Executing query from ${query.from} to ${query.to}`);

            const t0 = new Date();
            await runQuery(planner, query);
            const responseTime = new Date() - t0;

            console.log(`\tresponse time = ${responseTime} ms`);

            if (results[j]) {
                results[j].art += responseTime;
            } else {
                results[j] = {
                    query: {
                        from: firstLeg.steps[0].startLocation,
                        to: lastLeg.steps[lastLeg.steps.length - 1].stopLocation,
                        departureTime: firstLeg.steps[0].startTime
                    },
                    art: responseTime
                };
            }
            console.log('*********************************************************');
        }
    }
    // Calculate averages
    let total = 0;
    results.forEach(r => {
        r.art = r.art / 10;
        total += r.art;
    });

    total = total / results.length;

    fs.writeFileSync(`${config.rootPath}/results/${source}/results_${test}.json`,
        JSON.stringify({ TOTAL: total, results: results }, null, 3), 'utf8');
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