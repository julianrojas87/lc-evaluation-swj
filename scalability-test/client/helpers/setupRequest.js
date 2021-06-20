module.exports = (req, { stops, log }) => {
    const from = stops[req.from];
    const to = stops[req.to];
    const depDateTime = new Date(req.time);

    const queryString =
        `?fromPlace=${from.lat},${from.lon}` +
        `&toPlace=${to.lat},${to.lon}` +
        `&time=${depDateTime.getHours()}:${depDateTime.getMinutes()}` +
        `&date=${depDateTime.getMonth() + 1}-${depDateTime.getDate()}-${depDateTime.getFullYear()}` +
        `&mode=TRANSIT,WALK`;

    if(log) console.log(queryString);
    
    req.path += queryString;
    return req;
}