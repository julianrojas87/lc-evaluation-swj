import fs, { readFileSync } from 'fs';
import config from '../config.js';

async function run() {
    for (const source of config.sources) {
        const results = [];
        const fragments = fs.readdirSync(`${config.rootPath}/fragmentations/${source.name}`);
        fragments.sort((a, b) => {
            return parseInt(a) - parseInt(b);
        });

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

        for(let i = 0; i < fragments.length; i++) {
            let resPath = `${config.rootPath}/results/${source.name}/results_`;
            if(i === 0) {
                resPath += 'min.json';
            } else {
                resPath += `${fragments[i]}.json`;
            }

            const res = JSON.parse(readFileSync(resPath, 'utf-8'));

            // Extract response_time/connection, pages fetched and bytes transferred
            const crts = [];
            const pfs = [];
            const bts = [];

            for(const q of res.results) {
                if (q.timePerConnection) crts.push(q.timePerConnection);
                pfs.push(q.pagesFetched);
                bts.push(q.bytesTransferred);
            }

            crts.sort();
            pfs.sort();
            bts.sort();

            art += `,${fragments[i]},${res.averageResponseTime}`;
            rtp10 += `,${fragments[i]},${res.p10}`;
            rtp50 += `,${fragments[i]},${res.p50}`;
            rtp75 += `,${fragments[i]},${res.p75}`;
            rtp90 += `,${fragments[i]},${res.p90}`;
            acrt += `,${fragments[i]},${crts.reduce((p, c) => p + c) / crts.length}`;
            crtp90 += `,${fragments[i]},${crts[Math.round(crts.length * 0.9)]}`;
            apf += `,${fragments[i]},${pfs.reduce((p, c) => p + c) / pfs.length}`
            pfp90 += `,${fragments[i]},${pfs[Math.round(pfs.length * 0.9)]}`
            abt += `,${fragments[i]},${bts.reduce((p, c) => p + c) / bts.length}`
            btp90 += `,${fragments[i]},${bts[Math.round(bts.length * 0.9)]}`
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

        fs.writeFileSync(`${config.rootPath}/results/${source.name}/results.csv`, results.join('\n'), 'utf8');
    }
}

run();