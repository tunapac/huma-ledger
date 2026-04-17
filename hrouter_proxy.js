const http = require('http');
const https = require('https');

const PORT = 8888;
const AD_DOMAINS = ['doubleclick.net', 'googleadservices.com', 'ads.google.com', 'facebook.com/tr'];

const server = http.createServer((req, res) => {
    const url = new URL(req.url);
    
    // 1. AD BLOCKER: If it's an ad, kill the request immediately to save data
    if (AD_DOMAINS.some(domain => url.hostname.includes(domain))) {
        console.log(`🚫 BLOCKED AD: ${url.hostname}`);
        res.writeHead(204);
        return res.end();
    }

    // 2. DATA COMPRESSION REQUEST: Ask the server for the smallest version
    req.headers['accept-encoding'] = 'gzip, deflate';

    const options = {
        hostname: url.hostname,
        port: url.port || (url.protocol === 'https:' ? 443 : 80),
        path: url.pathname + url.search,
        method: req.method,
        headers: req.headers
    };

    const proxy = (url.protocol === 'https:' ? https : http).request(options, (targetRes) => {
        res.writeHead(targetRes.statusCode, targetRes.headers);
        targetRes.pipe(res);
    });

    req.pipe(proxy);
    proxy.on('error', () => res.end());
});

server.listen(PORT, '127.0.0.1', () => {
    console.log(`🚀 H-Router Data-Saver Active on Port ${PORT}`);
    console.log(`Watching for Ad traffic to block...`);
});
