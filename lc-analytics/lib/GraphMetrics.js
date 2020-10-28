import config from '../config.js';
import Graph from 'graphology';
import fs from 'fs';
import readline from 'readline';
import { TimeVaryingGraph } from './TimeVaryingGraph.js';


export async function measureGraphMetrics(source) {
    // Time-Varying Graph
    const TVG = new TimeVaryingGraph();
    const stops = new Set();
    const connections = new Set();

    const connStream = readline.createInterface({
        input: fs.createReadStream(`${config.rootPath}/raw-lc/${source.path}`),
        crlfDelay: Infinity
    });

    let depTime = null;
    let currentGraph = null;

    for await (const rawCx of connStream) {
        const cx = JSON.parse(rawCx);
        // New depTime so new graph
        if (depTime !== cx.departureTime) {
            depTime = cx.departureTime;
            currentGraph = new Graph.MultiDirectedGraph();
            TVG.addGraph(depTime, currentGraph);
        }

        // Add vertexes and edge to the graph snapshot
        if (!currentGraph.hasNode(cx.departureStop)) currentGraph.addNode(cx.departureStop);
        if (!currentGraph.hasNode(cx.arrivalStop)) currentGraph.addNode(cx.arrivalStop);
        currentGraph.addEdge(cx.departureStop, cx.arrivalStop, {
            "id": cx['@id'],
            "duration": (new Date(cx.arrivalTime) - new Date(cx.departureTime)) / 1000
        });

        // Keep track of unique stops and connections for counting
        stops.add(cx.departureStop);
        stops.add(cx.arrivalStop);
        connections.add(cx['@id']);
    }

    connStream.close();

    // Add total count of vertexes and edges (stops and connections)
    TVG.V = stops.size;
    TVG.E = connections.size;

    //console.log(`${source.name},${TVG.V},${TVG.E},${TVG.getMinimumFragmentSize()},${TVG.calculateDegree()}`);
    console.log(`Public Transport Network: ${source.name}`);
    console.log(`Number of Stops: ${TVG.V}`);
    console.log(`Number of Connections: ${TVG.E}`);
    console.log(`Minimum fragment size: ${TVG.getMinimumFragmentSize()}`);
    console.log(`Average Degree: ${TVG.calculateDegree()}`);
    console.log(`Average Connection duration: `);
    console.log('*******************************************************');

    return TVG;
}
