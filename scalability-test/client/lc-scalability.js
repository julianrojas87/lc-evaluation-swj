const fs = require('fs');
const util = require('util');
const path = require('path');
const { URL } = require('url');
const autocannon = require('autocannon');
const fetch = require('node-fetch');

const readFile = util.promisify(fs.readFile);

// Parameters to be configured from environment
const serverURI = process.argv[2] || 'http://localhost';
const serverPort = process.argv[3] || 3000;
const operator = process.argv[4] || 'thailand-greenbus';
const iterations = process.argv[5] || 1;
const subset = process.argv[6] || 100;

// Increasing amount of concurrent clients to evaluate
const concurrencies = process.argv[7] ? process.argv[7].split(',').map(c => parseInt(c)) : [1, 2, 5, 10, 20, 50, 100];
const workers = process.argv[8] ? process.argv[8].split(',').map(w => parseInt(w)) : [1, 2, 5, 10, 10, 10, 10];

// Request logging flag
const log = process.argv[9] === 'true';

async function getQuerySet() {
    return JSON.parse(await readFile(path.join(process.cwd(), 'query-sets', operator, 'urls.json'), 'utf8'));
}

async function toggleRecording(record, index) {
    if (record) {
        await fetch(`${serverURI}:3001?command=start&operator=${operator}&concurrency=${concurrencies[index]}`);
    } else {
        await fetch(`${serverURI}:3001?command=stop`);
    }
}

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function run() {
    const results = [];
    // Load query set
    const queries = (await getQuerySet()).slice(0, subset - 1);
    // Make sure every client executes all the query set
    const reqs = queries.map(q => {
        const lcUrl = new URL(q);
        return {
            method: 'GET',
            path: lcUrl.pathname,
            depTime: lcUrl.searchParams.get('departureTime'),
            setupRequest: path.join(process.cwd(), 'helpers', 'setupRequest'),
            onResponse: path.join(process.cwd(), 'helpers', 'onResponse')
        };
    });

    // Start evaluation loop
    for (let i = 0; i < concurrencies.length; i++) {
        // Command stats recording on server
        await toggleRecording(true, i);
        await timeout(5000);

        console.log(`------------------RUNNING LOAD TEST WITH C=${concurrencies[i]} concurrent clients-------------------`);
        // Initialize autocannon
        const result = await autocannon({
            url: `${serverURI}:${serverPort}`,
            initialContext: { log: log },
            connections: concurrencies[i],
            workers: workers[i],
            pipelining: 1,
            amount: concurrencies[i] * iterations * queries.length, // repeat query set {iterations} times per client
            timeout: 10, // 10 seconds timeout for every request
            requests: reqs
        });
        console.log(`----------------RESULTS FOR LOAD TEST C=${concurrencies[i]}-----------------`);
        console.log(result);
        results.push(result);
        // Wait 1 minute before stopping stats recording to allow for pending requests to finish
        await timeout(60000);
        // Stop stats recording on server
        await toggleRecording(false);
    }
}

run();