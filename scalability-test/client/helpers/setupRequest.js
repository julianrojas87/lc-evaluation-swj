module.exports = (req, { stops }) => {
    const from = stops[req.from];
    const to = stops[req.to];
    const depDateTime = new Date(req.time);

    const queryString =
        `?fromPlace=${from.lat},${from.lon}` +
        `&toPlace=${to.lat},${to.lon}` +
        `&time=${depDateTime.getHours()}:${depDateTime.getMinutes()}` +
        `&date=${depDateTime.getDate()}-${depDateTime.getMonth() + 1}-${depDateTime.getFullYear()}` +
        `&mode=TRANSIT,WALK`;

    req.path += queryString;
    return req;
}