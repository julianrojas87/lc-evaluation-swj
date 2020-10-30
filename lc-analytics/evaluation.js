import config from './config.js';
import fs from 'fs';
import { runBenchmark } from './lib/RoutePlanningPerformance.js';

async function run() {
    if(!fs.existsSync(`${config.rootPath}/results`)) fs.mkdirSync(`${config.rootPath}/results`);
    for (const source of config.sources) {
        const querySet = fs.readFileSync(`${config.rootPath}/query-sets/${source.name}/query-set.json`, 'utf8');
        await runBenchmark(source, JSON.parse(querySet));
    }
}

run();