import degree from 'graphology-metrics/degree.js';

export class TimeVaryingGraph {
    constructor() {
        this._V = 0; // total number of stops
        this._E = 0; // total number of connections
        this._graphs = {}; // Sequence of graph snapshots
    }

    addGraph(key, g) {
        this.graphs[key] = g;
    }

    getMinimumFragmentSize() {
        let size = 0;
        let bg = null;

        for (const key of Object.keys(this.graphs)) {
            const g = this.graphs[key];
            if (g.size > size) {
                size = g.size;
                bg = g;
            }
        }

        return bg.size;
    }

    calculateDegree() {
        if (this.V > 0) {
            let totalDegree = 0;
            for (const key of Object.keys(this.graphs)) {
                const g = this.graphs[key];
                const dgs = degree(g);
                let avd = 0;

                for(const k of Object.keys(dgs)) {
                    avd += dgs[k];
                }

               totalDegree += avd / this.V; // Snapshot avg degree 
            }
            return totalDegree / Object.keys(this.graphs).length; // Total avg degree of the TVG
        } else {
            throw new Error('Cannot calculate degree without the graph\'s total amount of vertexes');
        }
    }

    calculateAvgConnectionDuration() {
        
    }

    get graphs() {
        return this._graphs;
    }

    get V() {
        return this._V;
    }

    set V(v) {
        this._V = v;
    }

    get E() {
        return this._E;
    }

    set E(e) {
        this._E = e;
    }
}