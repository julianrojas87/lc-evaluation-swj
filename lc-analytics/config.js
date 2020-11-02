export default {
    rootPath: "/groups/ilabt-imec-be/openplanner/ptn-evaluation",
    fragmentations: [5, 10, 50, 100, 300, 500, 1000, 3000, 5000, 10000, 20000, 30000],
    lcServer: "http://localhost:3000",
    lcDataPath: "/users/jrojasme/lc-data",
    sources: [
        {
            "name": "nmbs",
            "path": "nmbs_filtered.json",
            "busiestDay": "2020-11-12"
        },
        {
            "name": "amsterdam-gvb",
            "path": "amsterdam_filtered.json",
            "busiestDay": "2020-10-16"
        },
        {
            "name": "auckland-ferry",
            "path": "auckland-ferry_filtered.json",
            "busiestDay": "2020-10-16"
        },
        {
            "name": "auckland-waiheke",
            "path": "auckland-waiheke_filtered.json",
            "busiestDay": "2020-10-14"
        },
        {
            "name": "chicago-cta",
            "path": "chicago_filtered.json",
            "busiestDay": "2020-09-03"
        },
        {
            "name": "delijn",
            "path": "delijn_filtered.json",
            "busiestDay": "2020-09-11"
        },
        {
            "name": "deutsche-bahn",
            "path": "deutsche-bahn_filtered.json",
            "busiestDay": "2018-12-12"
        },
        {
            "name": "flixbus",
            "path": "flixbus_filtered.json",
            "busiestDay": "2020-09-12"
        },
        {
            "name": "helsinki-hsl",
            "path": "helsinki_filtered.json",
            "busiestDay": "2020-10-02"
        },
        {
            "name": "kobe-subway",
            "path": "kobe-subway_filtered.json",
            "busiestDay": "2017-08-08"
        },
        {
            "name": "london-tube",
            "path": "london-tube_filtered.json",
            "busiestDay": "2017-04-28"
        },
        {
            "name": "madrid-bus",
            "path": "madrid-bus_filtered.json",
            "busiestDay": "2020-09-24"
        },
        {
            "name": "nairobi-sacco",
            "path": "nairobi_filtered.json",
            "busiestDay": "2018-03-03"
        },
        {
            "name": "nl-waterbus",
            "path": "nl-waterbus_filtered.json",
            "busiestDay": "2020-10-15"
        },
        {
            "name": "new-york-mtabc",
            "path": "nyc_filtered.json",
            "busiestDay": "2020-12-02"
        },
        {
            "name": "nz-bus",
            "path": "nz-bus_filtered.json",
            "busiestDay": "2020-10-16"
        },
        {
            "name": "renfe",
            "path": "renfe_filtered.json",
            "busiestDay": "2020-09-23"
        },
        {
            "name": "sf-bart",
            "path": "sf-bart_filtered.json",
            "busiestDay": "2020-09-24"
        },
        {
            "name": "sncf",
            "path": "sncf_filtered.json",
            "busiestDay": "2020-09-25"
        },
        {
            "name": "stib",
            "path": "stib_filtered.json",
            "busiestDay": "2020-10-12"
        },
        {
            "name": "sydney-trainlink",
            "path": "sydney-trainlink_filtered.json",
            "busiestDay": "2020-10-16"
        },
        {
            "name": "tec",
            "path": "tec_filtered.json",
            "busiestDay": "2020-10-14"
        },
        {
            "name": "thailand-greenbus",
            "path": "thailand-greenbus_filtered.json",
            "busiestDay": "2018-05-25"
        }
    ]
}
