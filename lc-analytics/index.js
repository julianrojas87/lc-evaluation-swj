import fs from 'fs';
import config from './config.js';
import { measureGraphMetrics } from './lib/GraphMetrics.js';
import { fragmentPTN } from './lib/Fragmentator.js';
import { findSolvableQueries } from './lib/RandomQueryExtractor.js';

async function run() {
        for (const source of config.sources) {
            //console.log('Public Transport Network,Number of Stops,Number of Connections,Minimum fragment size,Average Degree');
            const { TVG, stops } = await measureGraphMetrics(source);
            await fragmentPTN(source, TVG);
            if(!fs.existsSync(`${config.rootPath}/query-sets`)) fs.mkdirSync(`${config.rootPath}/query-sets`);
            await findSolvableQueries(source, stops);
        }
    }

run();