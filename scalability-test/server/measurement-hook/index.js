const http = require('http');
const util = require('util');
const { URL } = require('url');
const child_process = require('child_process');

const exec = util.promisify(child_process.exec);

http.createServer(async (req, res) => {
    const urlObj = new URL(req.url, `http://${req.headers.host}`);
    const command = urlObj.searchParams.get('command');
    const operator = urlObj.searchParams.get('operator');
    const concurrency = urlObj.searchParams.get('concurrency');

    if (command === 'start') {
        exec(`sudo ../recordstats.sh > ../../results/${operator}/${concurrency}.csv`);
    }

    if (command === 'stop') {
        await exec('./restart_container.sh');
    }

    res.statusCode = 200
    res.end();
}).listen(3001);