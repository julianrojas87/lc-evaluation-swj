module.exports = (status, body, { log }) => {
    if (status === 200 && log) {
        const jb = JSON.parse(body);

        console.log(jb.plan ? jb.plan : jb['@graph'][0]);
    }
}