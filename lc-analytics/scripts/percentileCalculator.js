import config from '../config.js';
import fs from 'fs';

function calculatePercentile() {

    for (const source of config.sources) {
        const resultSet = fs.readdirSync(`${config.rootPath}/results/${source.name}`);
        const percentiles = [];

        resultSet.sort((a, b) => {
            const na = parseInt(a.substring(a.indexOf('_') + 1, a.indexOf('.')));
            const nb = parseInt(b.substring(b.indexOf('_') + 1, b.indexOf('.')));
            return na - nb;
        });

        for(const rpath of resultSet) {
            const results = JSON.parse(fs.readFileSync(`${config.rootPath}/results/${source.name}/${rpath}`)).results;
            results.sort((a, b) => {
                return a.art - b.art;
            });
            
            const percentile = Math.round(results.length * 0.1);
            percentiles.push(results[percentile].art);
        }
        
        console.log(`${source.name}, ${percentiles.join(', ')}`);
    }

}

calculatePercentile();