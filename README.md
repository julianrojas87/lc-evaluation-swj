# _Linked Connections_ evaluation - Semantic Web Journal paper
Evaluation data, results and tools for the paper titled `Publishing planned, live and historical public transport data on the Web with the Linked Connections Framework`, submitted for the [Special Issue on Transport Data on the Web of the Semantic Web Journal](http://www.semantic-web-journal.net/blog/call-papers-special-issue-transport-data-web). 

## Evaluation process

Here we describe the set of steps taken to execute the evaluation and obtain the results reported on the paper.

### 1. Raw data

Our evaluation was performed on a set of 22 different and real public transport networks from around the world. The raw data of these networks is originally formatted as GTFS data dumps, which we make available at: https://cloud.ilabt.imec.be/index.php/s/7PeH9L3MijrHCRi

### 2. Converting GTFS to _Linked Connections_

The conversion of a GTFS source to Linked Connections is done through the [`gtfs2lc`](https://github.com/linkedconnections/gtfs2lc/tree/development) Node.js library (we used the `development` branch). We took the following steps to convert a particular GTFS source:

- Unzip the GTFS source: 

  ```bash
  unzip {source}.zip
  ```

- Run preparation script that makes sure data is consistent and properly ordered for conversion: 

  ```bash
  ./gtfs2lc/bin/gtfs2lc-sort.sh /path/to/{source}
  ```

- Execute conversion process using the [baseURIs.json](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/base-uris.json) file on this repository as input for the unique identifiers scheme: 

  ```bash
  node ./gtfs2lc/bin/gtfs2lc.js -f jsonld -b baseURIs.json -o /path/to/output/folder /path/to/{source}
  ```

- Sort resulting Linked Connections by departure time:

  ```bash
  sort -T ./ -t \" -k 19 {lc-source.json} > {lc-source_sorted.json}
  ```

- Compress to save disk space:

  ```bash
  gzip path/to/{lc-source_sorted.json}
  ```

### 3. Extract busiest day _Linked Connections_

For each network, we used the busiest day of the schedule as a representative subset of the entire data source. The busiest day is the day with the highest amount of trips. We used the [`peartree`](https://github.com/kuanb/peartree) Python library to find the busiest day for each network. We provide the [busy_days.py](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/busiest-days/busy_days.py) Python script and also the [obtained results](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/busiest-days/busiest_days.txt) for every network.

Knowing the busiest day of a network, we can then filter the relevant Linked Connections as follows:

```bash
zcat {lc-source_sorted.json.gz} | grep departureTime\":\"{busiest_date} > {source_filtered.json}
```

We provide already the set of busiest day Linked Connections for every network at https://cloud.ilabt.imec.be/index.php/s/brWo8jgwgHYcE6k

### 4. Route planning performance

For each network, we measured the evaluation performance of _Earliest Arrival Time_ route planning queries, using route planning Javascript library [`planner.js`](https://planner.js.org/) (we used the [`swj-eval`](https://github.com/openplannerteam/planner.js/tree/swj-eval) branch). The overall results are already available in the [results](https://github.com/julianrojas87/lc-evaluation-swj/tree/main/results) folder of this repository. The steps to reproduce this evaluation are described next.

#### 4.1 Create fragmentation sets

The first step consists on fragmenting the Linked Connection collections obtained from the previous step, in uniform fragments of fixed size (in terms of number of connections). 

For this we use the [`lc-analytics`](https://github.com/julianrojas87/lc-evaluation-swj/tree/main/lc-analytics) Node.js application, bundled within this repository.  This application needs to be installed:

```bash
cd lc-analytics
npm install
```

and configured using the [config.js](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/lc-analytics/config.js) file.  Is necessary to set the `rootPath` property with the path to a parent folder where all results will be stored. 

This parent folder must have a folder named _raw-lc_, containing the set of Linked Connection collections obtained in step 3. The rest of the parameters are already pre-configured and may be adjusted only in further steps.

The fragmentation process is then executed with the following command:

```bash
node lc-analytics/scripts/fragmentator.js
```

The results of this step will be stored in a folder called _fragmentations_ inside the `rootPath` parent folder. 

#### 4.2 Setup a _Linked Connections_ server

In this step, we setup a Node.js [Linked Connections server](https://github.com/linkedconnections/linked-connections-server/tree/swj-evaluation) over all the networks (we used the `swj-evaluation` branch). Once installed we need to configure the server, for which we already provide a configuration file called [datasets_config.json](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/datasets_config.json).  Follow these steps:

- Adjust the value of the `lcDataPath` property of [config.js](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/lc-analytics/config.js) to a folder of your choice. This folder will contain one sub-folder for every configured fragmentation size. 

- Create a folder called `raw-data` inside your main parent folder (defined in `rootPath` of config.js) and put all the GTFS sources there. This is to provide the stops/stations data, needed for solving route planning queries later.

- Run the following script to organize the folder structure needed by the server:

  ```bash
  node lc-analytics/scripts/organizeFolders.js
  ```

- Adjust the value of the `storage` property of the server _datasets_config.json_ to the path of any of the fragmentation sub-folders created inside of  `lcDataPath`.

- Start the server:

  ```bash
  ./linked-connections-server/bin/web-server
  ```

  **note:** the server needs additional network configuration that can be checked as part of its documentation.

#### 4.3 Generate random queries

To perform the route planning query evaluation we first need a set of queries for each network that are possible to be resolved. We created a Node.js script that generate sets of queries for a network, by testing random pairs of stops departing at also random times. The script uses planner.js to perform the tests. We already provide a [complete set of queries](https://github.com/julianrojas87/lc-evaluation-swj/tree/main/query-sets) for each network in this repository, but to execute the script proceed as follows:

```bash
node lc-analytics/scripts/generateQueries.js
```

The script will create a folder named _query-sets_ inside the folder indicated by the `rootPath` configuration property.

#### 4.4 Run the evaluation

With a set of queries and a Linked Connections server up and running the evaluation can be executed for a single network as follows:

```bash
node lc-analytics/scripts/evaluation.js {transport_network} {fragment_size} {repetitions}
```

`{transport_network}` refers to the name of the network (e.g. `flixbus`). `{fragment_size}` is the fragmentation size that will be tested and `{repetitions}` is the number of times the query set will be replayed. The raw results will be stored in the _results_ folder inside the folder indicated by the `rootPath` configuration property.

#### 4.5 Extract results

Once all the evaluations have been completed, results can be collected into a single CSV file per network that contains different measurements per fragmentation. To generate this file execute the following script:

```bash
node lc-analytics/scripts/extractResutls.js
```

A file called _results.csv_ will be created next to the raw results of each network. We already provide such file for every network.

#### 4.6 Visualize results

We provide 3 Python scripts that correspond to figures 6, 7 and 8 in the paper. Scripts can be found in the [plots](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/plots) folder of this repository.

### 5. Measure network graph metrics

One of the main contributions of our paper is the cross-correlation of particular topological network properties (size, degree, density, clustering coefficient and connection duration) with the measured route planning query evaluation performance. The metrics can be calculated by running the following script:

```bash
node lc-analytics/scripts/graphMetrics.js
```

The results will be printed on console in a CSV format. We already provide the set of measured metrics in this [_graph-metrics.csv_](https://github.com/julianrojas87/lc-evaluation-swj/blob/main/results/graph-metrics.csv) file.