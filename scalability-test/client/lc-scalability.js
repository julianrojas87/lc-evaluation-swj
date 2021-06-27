const fs = require('fs');
const util = require('util');
const path = require('path');
const { URL } = require('url');
const autocannon = require('autocannon');
const fetch = require('node-fetch');
const { Worker } = require("worker_threads");

const readFile = util.promisify(fs.readFile);

// Parameters to be configured from environment
const server = process.argv[2];
const serverURI = process.argv[3] || 'http://localhost';
const serverPort = process.argv[4] || 3000;
const operator = process.argv[5] || 'amsterdam-gvb';
const iterations = process.argv[6] || 1;
const subset = process.argv[7] || 100;

// Increasing amount of concurrent clients to evaluate
const concurrencies = process.argv[8] ? process.argv[8].split(',').map(c => parseInt(c)) : [1, 2, 5, 10, 20, 50, 100];
const workers = process.argv[9] ? process.argv[9].split(',').map(w => parseInt(w)) : [1, 2, 5, 10, 10, 10, 10];

// Request logging flag
const log = process.argv[10] === 'true';

async function getURLSet() {
    return JSON.parse(await readFile(path.join(process.cwd(), 'query-sets', operator, 'urls.json'), 'utf8'));
}

async function getQuerySet() {
    return JSON.parse(await readFile(path.join(process.cwd(), 'query-sets', operator, 'query-set.json'), 'utf8'));
}

async function toggleRecording(record, index) {
    if (record) {
        await fetch(`${serverURI}:3001?command=start&operator=${operator}&concurrency=${concurrencies[index]}&server=${server}`);
    } else {
        await fetch(`${serverURI}:3001?command=stop`);
    }
}

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function runPlannerJS() {
    return new Promise(async resolve => {
        const plannerjs = new Worker('./helpers/plannerjs.js', {
            workerData: {
                server: `${serverURI}:${serverPort}`,
                operator: operator,
                querySet: await getQuerySet(),
                cycles: 1
            }
        });

        plannerjs.once('message', result => {
            console.log(result);
            resolve(result);
        });
    });
}

async function run() {
    const results = [];
    // Load query set
    const queries = (await getURLSet()).slice(0, subset - 1);
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

        let loadGenerator = null;

        if (concurrencies[i] > 1) {
            // Initialize autocannon only if 
            loadGenerator = autocannon({
                url: `${serverURI}:${serverPort}`,
                initialContext: { log: log },
                connections: concurrencies[i] - 1,
                workers: workers[i],
                pipelining: 1,
                duration: 86400, // Set a very long time so autocannon does not stop in the middle of the test
                requests: reqs
            });
        }

        // Initialize Planner.js worker
        results.push(await runPlannerJS());

        if (loadGenerator) {
            // Stop autocannon because planner.js finished already
            loadGenerator.stop();
        }

        // Wait 1 minute before stopping stats recording to allow for pending requests to finish
        await timeout(60000);
        // Stop stats recording on server
        await toggleRecording(false);
    }

    console.log(JSON.stringify(results));
}

run();