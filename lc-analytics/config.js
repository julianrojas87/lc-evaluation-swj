export default {
    rootPath: "/groups/ilabt-imec-be/openplanner/ptn-evaluation",
    fragmentations: [1, 2, 5, 10, 20, 50, 100, 500, 1000],
    lcServer: "http://localhost:3000",
    sources: [
        {
            "name": "nmbs",
            "path": "nmbs_filtered.json"
        },
	{
	   "name": "amsterdam-gvb",
	   "path": "amsterdam_filtered.json"
	},
	{
            "name": "auckland-ferry",
            "path": "auckland-ferry_filtered.json"
        },
	{
            "name": "auckland-waiheke",
            "path": "auckland-waiheke_filtered.json"
        },
	{
            "name": "chicago-cta",
            "path": "chicago_filtered.json"
        },
	{
            "name": "delijn",
            "path": "delijn_filtered.json"
        },
	{
            "name": "deutsche-bahn",
            "path": "deutsche-bahn_filtered.json"
        },
	{
            "name": "flixbus",
            "path": "flixbus_filtered.json"
        },
	{
            "name": "helsinki-hsl",
            "path": "helsinki_filtered.json"
        },
	{
            "name": "kobe-subway",
            "path": "kobe-subway_filtered.json"
        },
	{
            "name": "london-tube",
            "path": "london-tube_filtered.json"
        },
	{
            "name": "madrid-bus",
            "path": "madrid-bus_filtered.json"
        },
	{
            "name": "nairobi-sacco",
            "path": "nairobi_filtered.json"
        },
	{
            "name": "nl-waterbus",
            "path": "nl-waterbus_filtered.json"
        },
	{
            "name": "new-york-mtabc",
            "path": "nyc_filtered.json"
        },
	{
            "name": "nz-bus",
            "path": "nz-bus_filtered.json"
        },
	{
            "name": "renfe",
            "path": "renfe_filtered.json"
        },
	{
            "name": "sf-bart",
            "path": "sf-bart_filtered.json"
        },
	{
            "name": "sncf",
            "path": "sncf_filtered.json"
        },
	{
            "name": "stib",
            "path": "stib_filtered.json"
        },
	{
            "name": "sydney-trainlink",
            "path": "sydney-trainlink_filtered.json"
        },
	{
            "name": "tec",
            "path": "tec_filtered.json"
        },
	{
            "name": "thailand-greenbus",
            "path": "thailand-greenbus_filtered.json"
        }
    ]
}
