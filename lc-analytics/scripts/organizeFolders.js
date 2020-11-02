import config from '../config.js';
import fs from 'fs-extra';

async function run() {
    // Create LC folders for all fragmentations
    if (!fs.existsSync(config.lcDataPath)) fs.mkdirSync(config.lcDataPath);

    for (const source of config.sources) {
        const fragments = fs.readdirSync(`${config.rootPath}/fragmentations/${source.name}`);
        fragments.sort((a, b) => {
            return parseInt(a) - parseInt(b);
        });

        for (const [i, f] of fragments.entries()) {
            let root;
            if (i === 0) {
                root = `${config.lcDataPath}/min`;
            } else {
                root = `${config.lcDataPath}/${f}`;
            }

            if (!fs.existsSync(root)) {
                fs.mkdirSync(root);
                fs.mkdirSync(`${root}/datasets`);
                fs.mkdirSync(`${root}/linked_pages`);
                fs.mkdirSync(`${root}/stops`);
            }

            // Create and copy dataset
            fs.mkdirSync(`${root}/datasets/${source.name}`);
            fs.copyFileSync(`${config.rootPath}/raw-data/${source.name}.zip`, 
                `${root}/datasets/${source.name}/2020-10-30T19:00:00.000Z.zip`);

            // Create and copy fragmentation
            fs.mkdirsSync(`${root}/linked_pages/${source.name}/2020-10-30T19:00:00.000Z`);

            fs.copySync(`${config.rootPath}/fragmentations/${source.name}/${f}`, 
                `${root}/linked_pages/${source.name}/2020-10-30T19:00:00.000Z/`);

            // Create stops folder
            fs.mkdirSync(`${root}/stops/${source.name}`);
        }
    }
}

run();
