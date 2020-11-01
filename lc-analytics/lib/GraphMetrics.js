import config from '../config.js';
import Graph from 'graphology';
import fs from 'fs';
import readline from 'readline';
import degree from 'graphology-metrics/degree.js';
import density from 'graphology-metrics/density.js'

export async function measureGraphMetrics(source) {
    const stops = new Set();
    let connections = 0;
    let depConn = 0;
    let connectionsAlive = [];
    const TVG = {};

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
            // This connection belongs to a new graph, 
            // so calculate the metrics for the current and discard it to save memory.
            if (currentGraph) TVG[depTime] = calculateMetrics(currentGraph, depConn);
            depConn = 0;
            depTime = cx.departureTime;
            currentGraph = new Graph.MultiDirectedGraph();
        }

        // Remove expired connections
        connectionsAlive = connectionsAlive.filter(ac => {
            return new Date(ac.arrivalTime) >= new Date(depTime);
        });
        // Add current connection
        connectionsAlive.push(cx);
        // Counter for connections departing on this depTime
        depConn++;

        // Add vertexes and (alive) edges to the graph snapshot
        connectionsAlive.forEach(ac => {
            if (!currentGraph.hasNode(ac.departureStop)) currentGraph.addNode(ac.departureStop);
            if (!currentGraph.hasNode(ac.arrivalStop)) currentGraph.addNode(ac.arrivalStop);
            currentGraph.addEdge(ac.departureStop, ac.arrivalStop, {
                "id": ac['@id'],
                "duration": (new Date(ac.arrivalTime) - new Date(ac.departureTime)) / (1000 * 60)
            });
        });

        // Keep track of unique stops and connections for counting
        stops.add(cx.departureStop);
        stops.add(cx.arrivalStop);
        connections++;
    }

    connStream.close();

    // Complete metric values and calculate TVG averages
    let minFragmentSize = 0;
    let K = 0;
    let D = 0;
    let C = 0;
    let ACD = 0;

    for(const t in TVG) {
        const Gt = TVG[t];
        if(Gt.departingConnections > minFragmentSize) {
            minFragmentSize = Gt.departingConnections;
        }

        K += Gt.aggDegree / stops.size;
        D += density(stops.size, Gt.Et);
        C += Gt.aggC;
        ACD += Gt.ACD;
    }

    K = K / Object.keys(TVG).length;
    D = D / Object.keys(TVG).length;
    C = C / Object.keys(TVG).length;
    ACD = ACD / Object.keys(TVG).length;

    //console.log(`${source.name},${TVG.V},${TVG.E},${TVG.getMinimumFragmentSize()},${TVG.calculateDegree()}`);
    console.log(`Public Transport Network: ${source.name}`);
    console.log(`Number of Stops: ${stops.size}`);
    console.log(`Number of Connections: ${connections}`);
    console.log(`Minimum fragment size: ${minFragmentSize}`);
    console.log(`Average Degree: ${K}`);
    console.log(`Density: ${D}`);
    console.log(`Clustering Coefficient: ${C}`);
    console.log(`Average Connection duration: ${ACD} minutes`);
    console.log('*******************************************************');

    return { TVG: TVG, stops: stops };
}

function calculateMetrics(graph, dc) {
    return {
        departingConnections: dc,
        aggDegree: calculateAggDegree(graph),
        Et: graph.size,
        aggC: calculateAggClusteringCoefficient(graph),
        ACD: calculateAverageConnectionDuration(graph)
    };
}

function calculateAggDegree(G) {
    let aggK = 0;
    const dgs = degree(G);
    for (const k of Object.keys(dgs)) {
        aggK += dgs[k];
    }
    return aggK;
}

function calculateAggClusteringCoefficient(G) {
    let aggC = 0;
    for (const v of G.nodes()) {
        const neighbors = G.neighbors(v);
        let e = 0;
        if (neighbors.length > 1) {
            for (const n1 of neighbors) {
                for (const n2 of neighbors) {
                    if (G.hasEdge(n1, n2)) {
                        e++
                    };
                }
            }
            aggC += (2 * e) / (neighbors.length * (neighbors.length - 1));
        }
    }

    return aggC;
}

function calculateAverageConnectionDuration(G) {
    let ACD = 0;
    G.forEachEdge((key, attr) => {
        ACD += attr.duration;
    });
    return ACD / G.edges().length;
}