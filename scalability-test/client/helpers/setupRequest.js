module.exports = (req, { stops, log }) => {
    let queryString = '';
    if (stops) {
        const from = stops[decodeURIComponent(req.from)];
        const to = stops[decodeURIComponent(req.to)];
        const depDateTime = new Date(req.time);

        queryString =
            `?fromPlace=${from.lat},${from.lon}` +
            `&toPlace=${to.lat},${to.lon}` +
            `&time=${depDateTime.getUTCHours()}:${depDateTime.getUTCMinutes()}` +
            `&date=${depDateTime.getUTCMonth() + 1}-${depDateTime.getUTCDate()}-${depDateTime.getUTCFullYear()}` +
            `&mode=TRANSIT,WALK`;
    } else {
        queryString = `?departureTime=${req.depTime}`;
    }

    req.path += queryString;
    if (log) console.log(queryString);
    return req;
}