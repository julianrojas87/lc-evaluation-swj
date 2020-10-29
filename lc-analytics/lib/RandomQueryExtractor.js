import config from '../config.js';
import PlannerJS from 'plannerjs';
import fs from 'fs';

export async function findSolvableQueries(source, stops) {
    if(!fs.existsSync(`${config.rootPath}/query-sets/${source.name}`)) {
        fs.mkdirSync(`${config.rootPath}/query-sets/${source.name}`);
    }

    const querySet = [];
    const planner = new PlannerJS.FlexibleTransitPlanner();
    planner.addConnectionSource(`${config.lcServer}/${source.name}/connections`);
    planner.addStopSource(`${config.lcServer}/${source.name}/stops`);

    while (querySet.length < 100) {

        const query = {
            //from: "http://example.org/stations/8892007", // Gent-Sint-Pieters
            //to: "http://example.org/stations/8819406", // Zaventem
            //to: "http://example.org/stations/8200130",
            from: getRandomItem(stops),
            to: getRandomItem(stops),
            minimumDepartureTime: new Date('2020-11-12T00:00:00.000Z'),
            maximumArrivalTime: new Date('2020-11-13T07:00:00.000Z')
        }

        const path = await runQuery(planner, query);
        if (path) {
            querySet.push(path);
        }
    }

    fs.writeFileSync(`${config.rootPath}/query-sets/${source.name}/query-set.json`, JSON.stringify(querySet, null, 3), 'utf8');
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

function getRandomItem(set) {
    let items = Array.from(set);
    return items[Math.floor(Math.random() * items.length)];
}