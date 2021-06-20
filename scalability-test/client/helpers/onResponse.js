module.exports = (status, body, { log }) => {
    if (status === 200 && log) {
        console.log(JSON.parse(body).plan);
    }
}