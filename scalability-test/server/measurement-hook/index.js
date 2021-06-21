const http = require('http');
const { URL } = require('url');
const child_process = require('child_process');

const exec = util.promisify(child_process.exec);

http.createServer(async (req, res) => {
    const urlObj = new URL(req.url, `http://${req.headers.host}`);
    const command = urlObj.searchParams.get('command');
    const operator = urlObj.searchParams.get('operator');
    const concurrency = urlObj.searchParams.get('concurrency');

    if (command === 'start') {
        await exec(`sudo ../recordstats.sh > ../../results/${operator}/${concurrency}.csv`);
    }

    if (command === 'stop') {
        console.log('Stopping recording script...');
        await exec('sudo pkill -f recordstat');
        console.log('Stopping docker container...');
        await exec('sudo docker rm $(sudo docker ps -a -q)');
        console.log('Restarting docker container...');
        await exec('sudo docker run -p 8080:8080 --env-file=../conf.env --cpus=1 otp');
    }

    res.statusCode = 200
    res.end();
}).listen(3001);