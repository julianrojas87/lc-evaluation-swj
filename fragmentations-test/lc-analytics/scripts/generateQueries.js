import fs from 'fs';
import config from '../config.js';
import { calculateBasicTVG } from '../lib/GraphMetrics.js';
import { findSolvableQueries } from '../lib/RandomQueryExtractor.js';


async function run() {
    for (const source of config.sources) {
        if(!fs.existsSync(`${config.rootPath}/query-sets`)) fs.mkdirSync(`${config.rootPath}/query-sets`);
        await findSolvableQueries(source, (await calculateBasicTVG(source)).stops);
    }
}

run();