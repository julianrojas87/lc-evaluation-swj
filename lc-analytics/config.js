export default {
    rootPath: "/groups/ilabt-imec-be/openplanner/ptn-evaluation",
    fragmentations: [5, 10, 50, 100, 300, 500, 1000, 3000, 5000, 10000, 20000, 30000],
    lcServer: "http://localhost:3000",
    lcDataPath: "/users/jrojasme/lc-data",
    sources: [
        {
            "name": "nmbs",
            "path": "nmbs_filtered.json",
            "busiestDay": "2020-11-12",
            "smallestFragment": 94
        },
        {
            "name": "amsterdam-gvb",
            "path": "amsterdam_filtered.json",
            "busiestDay": "2020-10-16",
            "smallestFragment": 71
        },
        {
            "name": "auckland-waiheke",
            "path": "auckland-waiheke_filtered.json",
            "busiestDay": "2020-10-14",
            "smallestFragment": 5
        },
        {
            "name": "chicago-cta",
            "path": "chicago_filtered.json",
            "busiestDay": "2020-09-03",
            "smallestFragment": 164
        },
        {
            "name": "delijn",
            "path": "delijn_filtered.json",
            "busiestDay": "2020-09-11",
            "smallestFragment": 1861
        },
        {
            "name": "deutsche-bahn",
            "path": "deutsche-bahn_filtered.json",
            "busiestDay": "2018-12-12",
            "smallestFragment": 21
        },
        {
            "name": "flixbus",
            "path": "flixbus_filtered.json",
            "busiestDay": "2020-09-12",
            "smallestFragment": 386
        },
        {
            "name": "helsinki-hsl",
            "path": "helsinki_filtered.json",
            "busiestDay": "2020-10-02",
            "smallestFragment": 877
        },
        {
            "name": "kobe-subway",
            "path": "kobe-subway_filtered.json",
            "busiestDay": "2017-08-08",
            "smallestFragment": 16
        },
        {
            "name": "london-tube",
            "path": "london-tube_filtered.json",
            "busiestDay": "2017-04-28",
            "smallestFragment": 376
        },
        {
            "name": "madrid-bus",
            "path": "madrid-bus_filtered.json",
            "busiestDay": "2020-09-24",
            "smallestFragment": 247
        },
        {
            "name": "nairobi-sacco",
            "path": "nairobi_filtered.json",
            "busiestDay": "2018-03-03",
            "smallestFragment": 259
        },
        {
            "name": "nl-waterbus",
            "path": "nl-waterbus_filtered.json",
            "busiestDay": "2020-10-15",
            "smallestFragment": 7
        },
        {
            "name": "new-york-mtabc",
            "path": "nyc_filtered.json",
            "busiestDay": "2020-12-02",
            "smallestFragment": 130
        },
        {
            "name": "nz-bus",
            "path": "nz-bus_filtered.json",
            "busiestDay": "2020-10-16",
            "smallestFragment": 59
        },
        {
            "name": "renfe",
            "path": "renfe_filtered.json",
            "busiestDay": "2020-09-23",
            "smallestFragment": 27
        },
        {
            "name": "sf-bart",
            "path": "sf-bart_filtered.json",
            "busiestDay": "2020-09-24",
            "smallestFragment": 15
        },
        {
            "name": "sncf",
            "path": "sncf_filtered.json",
            "busiestDay": "2020-09-25",
            "smallestFragment": 180
        },
        {
            "name": "stib",
            "path": "stib_filtered.json",
            "busiestDay": "2020-10-12",
            "smallestFragment": 189
        },
        {
            "name": "sydney-trainlink",
            "path": "sydney-trainlink_filtered.json",
            "busiestDay": "2020-10-16",
            "smallestFragment": 7
        },
        {
            "name": "tec",
            "path": "tec_filtered.json",
            "busiestDay": "2020-10-14",
            "smallestFragment": 1207
        },
        {
            "name": "thailand-greenbus",
            "path": "thailand-greenbus_filtered.json",
            "busiestDay": "2018-05-25",
            "smallestFragment": 16
        }
    ]
}
