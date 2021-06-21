const http = require('http');
const { URL } = require('url');
const { exec } = require('child_process');

http.createServer((req, res) => {
    const urlObj = new URL(req.url, `http://${req.headers.host}`);
    const command = urlObj.searchParams.get('command');
    const operator = urlObj.searchParams.get('operator');
    const concurrency = urlObj.searchParams.get('concurrency');

    if (command === 'start') {
        exec(`sudo ../recordstats.sh > ../../results/${operator}/${concurrency}.csv`);
    }

    if (command === 'stop') {
        exec(`sudo pkill -f recordstat`);
    }

    res.statusCode = 200
    res.end();
}).listen(3001);
