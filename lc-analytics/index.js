import config from './config.js';
import { measureGraphMetrics } from './lib/GraphMetrics.js';
import { fragmentPTN } from './lib/Fragmentator.js'; 

async function run() {
        for (const source of config.sources) {
            //console.log('Public Transport Network,Number of Stops,Number of Connections,Minimum fragment size,Average Degree');
            const minCxs = await measureGraphMetrics(source);
            await fragmentPTN(source, minCxs);
        }
    }

run();