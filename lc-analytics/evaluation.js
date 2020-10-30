import config from './config.js';
import fs from 'fs';
import { runBenchmark } from './lib/RoutePlanningPerformance.js';

async function run() {
    if (!fs.existsSync(`${config.rootPath}/results`)) fs.mkdirSync(`${config.rootPath}/results`);
    const source = process.argv[process.argv.length - 2];
    const set = process.argv[process.argv.length - 1];
    const querySet = fs.readFileSync(`${config.rootPath}/query-sets/${source}/query-set.json`, 'utf8');
    await runBenchmark(source, JSON.parse(querySet), set);
}

run();