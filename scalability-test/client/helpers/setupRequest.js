module.exports = (req, { stops, log }) => {
    const from = stops[req.from];
    const to = stops[req.to];
    const depDateTime = new Date(req.time);

    const queryString =
        `?fromPlace=${from.lat},${from.lon}` +
        `&toPlace=${to.lat},${to.lon}` +
        `&time=${depDateTime.getUTCHours()}:${depDateTime.getUTCMinutes()}` +
        `&date=${depDateTime.getUTCMonth() + 1}-${depDateTime.getUTCDate()}-${depDateTime.getUTCFullYear()}` +
        `&mode=TRANSIT,WALK`;

    if(log) console.log(queryString);
    
    req.path += queryString;
    return req;
}