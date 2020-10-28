import fs from 'fs';
import readline from 'readline';
import config from '../config.js';
import { PaginatorStream } from './PaginatorStream.js';

export async function fragmentPTN(source, tvg) {
    const fragmentsPath = `${config.rootPath}/fragmentations/${source.name}`;
    if (!fs.existsSync(fragmentsPath)) {
        fs.mkdirSync(fragmentsPath);
    }

    const minFragSize = tvg.getMinimumFragmentSize();

    for (const x of config.fragmentations) {
        const size = x * minFragSize;
        const path = `${fragmentsPath}/${size}`;

        if (!fs.existsSync(path) && size <= tvg.E) {
            fs.mkdirSync(path);
            const connStream = readline.createInterface({
                input: fs.createReadStream(`${config.rootPath}/raw-lc/${source.path}`),
                crlfDelay: Infinity
            });
            const paginator = new PaginatorStream(path, size, tvg);

            for await (const cx of connStream) {
                paginator.write(JSON.parse(cx));
            }
            connStream.close();
            paginator.end();
        }
    }
}
