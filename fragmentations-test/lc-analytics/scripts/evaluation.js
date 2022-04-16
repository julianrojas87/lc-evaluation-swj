import config from '../config.js';
import fs from 'fs';
import { runBenchmark } from '../lib/RoutePlanningPerformance.js';

async function run() {
    const set = process.argv[process.argv.length - 3];
    const cycles = process.argv[process.argv.length - 2];
    const latency = process.argv[process.argv.length - 1];

    if (!fs.existsSync(`${config.rootPath}/results`)) fs.mkdirSync(`${config.rootPath}/results`);

    for (const s of config.sources) {
        const source = s.name;
        const querySet = fs.readFileSync(`${config.rootPath}/query-sets/${source}/query-set.json`, 'utf8');
        if (!fs.existsSync(`${config.rootPath}/results/${source}`)) fs.mkdirSync(`${config.rootPath}/results/${source}`);
        // Skip if results already exist
        if (!fs.existsSync(`${config.rootPath}/results/${source}/results_${set}.json`)) {
            await runBenchmark(source, JSON.parse(querySet), set, cycles, latency);
        }
    }
}

run();