import fs, { readFileSync } from 'fs';
import config from '../config.js';

async function run() {
    for (const source of config.sources) {
        const results = [];
        const resFiles = fs.readdirSync(`${config.rootPath}/results/${source.name}`)
            .filter(f => f.endsWith('.json') && f !== 'results_min.json');

        resFiles.sort((a, b) => {
            return getFragmentation(a) - getFragmentation(b);
        });

        resFiles.unshift('results_min.json');

        let art = `${source.name},average_response_time`;
        let rtp10 = `${source.name},response_time_p10`;
        let rtp50 = `${source.name},response_time_p50`;
        let rtp75 = `${source.name},response_time_p75`;
        let rtp90 = `${source.name},response_time_p90`;
        let acrt = `${source.name},average_connection_response_time`;
        let crtp90 = `${source.name},connection_response_time_p90`;
        let apf = `${source.name},average_pages_fetched`;
        let pfp90 = `${source.name},pages_fetched_p90`;
        let abt = `${source.name},average_bytes_transferred`;
        let btp90 = `${source.name},bytes_transferred_p90`;
        let asc = `${source.name},average_scanned_connections`;
        let scp90 = `${source.name},scanned_connections_p90`;
        let scsd = `${source.name},scanned_connections_std_deviation`;

        const scannedMap = getScannedConnectionsMap(source);

        for (const [i, r] of resFiles.entries()) {
            const resPath = `${config.rootPath}/results/${source.name}/${r}`;
            const res = JSON.parse(readFileSync(resPath, 'utf-8'));

            // Extract response_time/connection, pages fetched, bytes transferred and scanned connections
            const rts = [];
            const crts = [];
            const pfs = [];
            const bts = [];
            const scs = [];

            for (const q of res.results) {
                if (q.timePerConnection) {
                    const scannedC = scannedMap.get(`${q.query.from}->${q.query.to}@${q.query.minimumDepartureTime}`);
                    rts.push(q.responseTime);
                    crts.push(q.responseTime / scannedC);
                    pfs.push(q.pagesFetched);
                    bts.push(q.bytesTransferred);
                    scs.push(scannedC);
                }
            }

            rts.sort((a, b) => a - b);
            crts.sort((a, b) => a - b);
            pfs.sort((a, b) => a - b);
            bts.sort((a, b) => a - b);
            scs.sort((a, b) => a - b);

            // Print distribution of response times for the first fragmentation only
            if (i === 0) console.log(source.name, scs);

            const frag = i === 0 ? source.smallestFragment : getFragmentation(r);

            art += `,${frag},${rts.reduce((p, c) => p + c) / rts.length}`;
            rtp10 += `,${frag},${rts[Math.round(rts.length * 0.1)]}`;
            rtp50 += `,${frag},${rts[Math.round(rts.length * 0.5)]}`;
            rtp75 += `,${frag},${rts[Math.round(rts.length * 0.75)]}`;
            rtp90 += `,${frag},${rts[Math.round(rts.length * 0.9)]}`;
            acrt += `,${frag},${crts.reduce((p, c) => p + c) / crts.length}`;
            crtp90 += `,${frag},${crts[Math.round(crts.length * 0.9)]}`;
            apf += `,${frag},${pfs.reduce((p, c) => p + c) / pfs.length}`;
            pfp90 += `,${frag},${pfs[Math.round(pfs.length * 0.9)]}`;
            abt += `,${frag},${bts.reduce((p, c) => p + c) / bts.length}`;
            btp90 += `,${frag},${bts[Math.round(bts.length * 0.9)]}`;
            asc += `,${frag},${scs.reduce((p, c) => p + c) / scs.length}`;
            scp90 += `,${frag},${scs[Math.round(scs.length * 0.9)]}`;
            scsd += `,${frag},${getStandardDeviation(scs)}`;
        }

        results.push(art);
        results.push(rtp10);
        results.push(rtp50);
        results.push(rtp75);
        results.push(rtp90);
        results.push(acrt);
        results.push(crtp90);
        results.push(apf);
        results.push(pfp90);
        results.push(abt);
        results.push(btp90);
        results.push(asc);
        results.push(scp90);
        results.push(scsd);

        fs.writeFileSync(`${config.rootPath}/results/${source.name}/results.csv`, results.join('\n'), 'utf8');
    }
}

function getFragmentation(file) {
    return parseInt(file.substring(file.indexOf('_') + 1, file.indexOf('.')));
}

function getScannedConnectionsMap(source) {
    const minPath = `${config.rootPath}/results/${source.name}/results_min.json`;
    const min = JSON.parse(readFileSync(minPath, 'utf-8'));
    const map = new Map();

    for (const q of min.results) {
        map.set(`${q.query.from}->${q.query.to}@${q.query.minimumDepartureTime}`, q.scannedConnections)
    }

    return map;
}

function getStandardDeviation(array) {
    const n = array.length
    const mean = array.reduce((a, b) => a + b) / n
    return Math.sqrt(array.map(x => Math.pow(x - mean, 2)).reduce((a, b) => a + b) / n)
}

run();