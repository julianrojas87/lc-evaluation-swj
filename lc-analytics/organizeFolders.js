import config from './config.js';
import fs from 'fs-extra';

async function run() {
    // Create LC folders for all fragmentations
    if (!fs.existsSync(config.lcDataPath)) fs.mkdirSync(config.lcDataPath);

    for (const source of config.sources) {
        for (const [i, f] of config.fragmentations.entries()) {
            const root = `${config.lcDataPath}/${f}`;
            if (!fs.existsSync(root)) {
                fs.mkdirSync(root);
                fs.mkdirSync(`${root}/datasets`);
                fs.mkdirSync(`${root}/linked_pages`);
                fs.mkdirSync(`${root}/stops`);
            }

            const fname = getFragmentName(i, source);
            if (fname) {
                // Create and copy dataset
                fs.mkdirSync(`${root}/datasets/${source.name}`);
                fs.copyFileSync(`${config.rootPath}/raw-data/${source.name}.zip`, `${root}/datasets/${source.name}/2020-10-30T19:00:00.000Z.zip`);

                // Create and copy fragmentation
                fs.mkdirsSync(`${root}/linked_pages/${source.name}/2020-10-30T19:00:00.000Z`);

                fs.copySync(`${config.rootPath}/fragmentations/${source.name}/${fname}`, `${root}/linked_pages/${source.name}/2020-10-30T19:00:00.000Z/`);
                // Create stops folder
                fs.mkdirSync(`${root}/stops/${source.name}`);
            }
        }
    }
}

function getFragmentName(i, source) {
    const fragmentations = fs.readdirSync(`${config.rootPath}/fragmentations/${source.name}`);
    fragmentations.sort((a, b) => {
        return parseInt(a) - parseInt(b);
    });
    return fragmentations[i];
}

run();
