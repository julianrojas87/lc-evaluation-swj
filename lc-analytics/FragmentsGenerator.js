import fs from 'fs';
import readline from 'readline';
import config from './config.js';

async function run() {
    for (const source of config.sources) {
        if(!fs.existsSync(`${config.rootPath}fragmentations/${source.name}`)) {
            fs.mkdirSync(`${config.rootPath}fragmentations/${source.name}`);
        }
    }
}

run();