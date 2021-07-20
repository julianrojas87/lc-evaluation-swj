const http = require('http');
const fs = require('fs');

const data = fs.readdirSync('../raw-live-data/');
var index = 0;

http.createServer((req, res) => {
    res.statusCode = 200;
    console.log(index);
    fs.readFile(`../raw-live-data/${data[index]}`, function (err, content) {
        res.write(content);
        res.end();
        if(index < data.length - 1) {
            index++;
        } else {
            index = 0;
        }
    });
}).listen(3001);