import config from '../config.js';
import { measureGraphMetrics } from '../lib/GraphMetrics.js';


async function run() {
        for (const source of config.sources) {
            console.log('pt_operator,total_stops,total_connections,smallest_fragment,average_degree,density,clustering_coefficient,average_connection_duration');
            await measureGraphMetrics(source);
        }
    }

run();