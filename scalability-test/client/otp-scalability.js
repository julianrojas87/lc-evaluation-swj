const fs = require('fs');
const util = require('util');
const path = require('path');
const autocannon = require('autocannon');
const fetch = require('node-fetch');

const readFile = util.promisify(fs.readFile);

// Parameters to be configured from environment
const serverURI = process.argv[2];
const operator = process.argv[3];
const concurrency = parseInt(process.argv[4]);
const workers = parseInt(process.argv[5]);


async function getQuerySet() {
    return JSON.parse(await readFile(path.join(process.cwd(), 'query-sets', operator, 'query-set.json'), 'utf8'));
}

async function getStopIndex() {
    const obj = {};
    const response = await fetch(`${serverURI}/otp/routers/default/index/stops/`);
    const stops = await response.json();
    for (const s of stops) {
        obj[`http://example.org/stations/${s.id.substring(s.id.indexOf(':') + 1)}`] = s;
    }
    return obj;
}

async function run() {
    // Load Stop index to figure precise geo coordinates of every stop
    const stopIndex = await getStopIndex();
    // Load query set
    const queries = await getQuerySet();
    // Make sure every client executes all the query set
    const reqs = queries.map(q => {
        return {
            method: 'GET',
            path: `/otp/routers/default/plan`,
            from: q.from,
            to: q.to,
            time: q.minimumDepartureTime,
            setupRequest: path.join(process.cwd(), 'helpers', 'setupRequest')
        };
    });

    // Initialize autocannon
    const result = await autocannon({
        url: serverURI,
        initialContext: { stops: stopIndex },
        connections: concurrency,
        workers: workers,
        pipelining: 2,
        amount: concurrency * queries.length,
        connectionRate: 1,
        requests: reqs
    });

    console.log(result);
}

run();