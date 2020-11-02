import config from '../config.js';
import PlannerJS from 'plannerjs';
import fs from 'fs';

export async function findSolvableQueries(source, stops) {
    if (!fs.existsSync(`${config.rootPath}/query-sets/${source.name}`)) {
        fs.mkdirSync(`${config.rootPath}/query-sets/${source.name}`);
    }

    if (!fs.existsSync(`${config.rootPath}/query-sets/${source.name}/query-set.json`)) {
        const querySet = new Map();
        const planner = new PlannerJS.FlexibleTransitPlanner();

        planner.addConnectionSource(`${config.lcServer}/${source.name}/connections`);
        planner.addStopSource(`${config.lcServer}/${source.name}/stops`);

        while (querySet.size < 100) {
            const departureTime = getRandomTime(new Date(`${source.busiestDay}T00:00:00.000Z`),
                new Date(`${source.busiestDay}T23:00:00.000Z`));
            // Set a big max arrival time to include long trips too
            const maximumArrivalTime = new Date(departureTime.getTime() + 90000000)

            const query = {
                from: getRandomStop(stops),
                to: getRandomStop(stops),
                minimumDepartureTime: departureTime,
                maximumArrivalTime: maximumArrivalTime
            }

            const path = await runQuery(planner, query);
            if (path) {
                console.log(query);
                querySet.set(`${query.from}->${query.to}`, query);
            }
        }

        fs.writeFileSync(`${config.rootPath}/query-sets/${source.name}/query-set.json`, 
            JSON.stringify([ ...querySet.values()], null, 3), 'utf8');
    }
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

function getRandomStop(stops) {
    return stops[Math.floor(Math.random() * stops.length)];
}

function getRandomTime(start, end) {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
}