
const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.writeHead(200, { 'Content-Type': 'application/json' });

    if (req.url === '/reward') {
        console.log("⚡ REWARD SIGNAL: +1.0000 Å synced to phone ledger.");
        res.end(JSON.stringify({ status: "SUCCESS" }));
    } else {
        res.end(JSON.stringify({ status: "H-ROUTER_ONLINE" }));
    }
});

server.listen(8888, () => {
    console.log("=========================================");
    console.log("   888+ UNIVERSAL H-ROUTER IS LIVE    ");
    console.log("   Listening for Extraction Chips...   ");
    console.log("=========================================");
});

