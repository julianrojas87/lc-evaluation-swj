const fs = require('fs');
const util = require('util');
const path = require('path');
const autocannon = require('autocannon');
const fetch = require('node-fetch');

const readFile = util.promisify(fs.readFile);

// Parameters to be configured from environment
const serverURI = process.argv[2] || 'http://localhost';
const serverPort = process.argv[3] || 8080;
const operator = process.argv[4] || 'amsterdam-gvb';

// Increasing amount of concurrent clients to evaluate
const concurrencies = [1, 2, 5, 10, 20, 50, 100, 200];
var workers = [1, 2, 5, 10, 10, 10, 10];

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function toggleRecording(record, index) {
    if (record) {
        await fetch(`${serverURI}:3001?command=start&operator=${operator}&concurrency=${concurrencies[index]}`);
    } else {
        await fetch(`${serverURI}:3001?command=stop`);
    }
}

async function getQuerySet() {
    return JSON.parse(await readFile(path.join(process.cwd(), 'query-sets', operator, 'query-set.json'), 'utf8'));
}

async function getStopIndex() {
    const obj = {};
    const response = await fetch(`${serverURI}:${serverPort}/otp/routers/default/index/stops/`);
    const stops = await response.json();
    for (const s of stops) {
        obj[`http://example.org/stations/${s.id.substring(s.id.indexOf(':') + 1)}`] = s;
    }
    return obj;
}

async function run() {
    const results = [];
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

    // Start evaluation loop
    for (let i = 0; i < concurrencies.length; i++) {
        // Command stats recording on server
        await toggleRecording(true, i);
        await timeout(2000);

        // Initialize autocannon
        const result = await autocannon({
            url: `${serverURI}:${serverPort}`,
            initialContext: { stops: stopIndex },
            connections: concurrencies[i],
            workers: workers[i],
            pipelining: 1,
            amount: concurrencies[i] * 3 * queries.length, // repeat query set 3 times per client
            connectionRate: 1,
            timeout: 120,
            requests: reqs
        });
        console.log(`----------------RESULTS FOR LOAD TEST C=${concurrencies[i]}-----------------`);
        console.log(result);
        results.push(result);
        // Wait 10s before stopping stats recording to allow for pending requests to finish
        await timeout(10000);
        // Stop stats recording on server
        await toggleRecording(false);
    }
    console.log(JSON.stringify(results));
}

run();