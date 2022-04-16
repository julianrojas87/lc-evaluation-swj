import fs from 'fs';
import readline from 'readline';
import { spawn } from 'child_process';
import config from '../config.js';
import { calculateBasicTVG } from '../lib/GraphMetrics.js';
import { PaginatorStream } from '../lib/PaginatorStream.js';

async function run() {
    if(!fs.existsSync(`${config.rootPath}/fragmentations`)) {
        fs.mkdirSync(`${config.rootPath}/fragmentations`);
    }
    
    for (const source of config.sources) {
        const TVG = await calculateBasicTVG(source);
        await fragmentPTN(source, TVG);
    }
}

async function fragmentPTN(source, TVG) {
    const fragmentsPath = `${config.rootPath}/fragmentations/${source.name}`;
    if (!fs.existsSync(fragmentsPath)) {
        fs.mkdirSync(fragmentsPath);
    }

    // Get fragments for min possible size
    const path = `${fragmentsPath}/${TVG.minFragmentSize}`;
    await fragment(source, path, TVG.minFragmentSize, TVG);

    // Fragment for all other configured sizes where possible
    for (const x of config.fragmentations) {
        const path = `${fragmentsPath}/${x}`;
        if (x >= TVG.minFragmentSize && x <= TVG.totalConnections) {
            await fragment(source, path, x, TVG);
        }
    }
}

async function fragment(source, path, size, TVG) {
    if (!fs.existsSync(path)) {
        fs.mkdirSync(path);
        const connStream = getReadInterface(source);
        const paginator = new PaginatorStream(path, size, TVG);
        for await (const cx of connStream) {
            paginator.write(JSON.parse(cx));
        }
        connStream.close();
        paginator.end();
        await compressAll(path);
    }
}

function getReadInterface(source) {
    return readline.createInterface({
        input: fs.createReadStream(`${config.rootPath}/raw-lc/${source.path}`),
        crlfDelay: Infinity
    });
}

function compressAll(path) {
    return new Promise(resolve => {
        spawn('find', ['.', '-type', 'f', '-exec', 'gzip', '{}', '+'], {
            cwd: path,
            stdio: 'ignore'
        }).on('close', () => resolve());
    });
}

run();
