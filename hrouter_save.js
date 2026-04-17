const http = require('http');
const https = require('https');

const PORT = 8888;
let totalSaved = 0; // In Bytes

const AD_BLOCK = ['doubleclick.net', 'google-analytics.com', 'ads.google.com', 'fbcdn.net'];

const server = http.createServer((req, res) => {
    const url = new URL(req.url, `http://${req.headers.host}`);
    
    // IF IT'S AN AD: We "Kill" it and count the savings (average ad is 150KB)
    if (AD_BLOCK.some(ad => url.hostname.includes(ad))) {
        totalSaved += 153600; // Adding 150KB to the "Saved" counter
        console.log(`🚫 AD KILLED! Saved: ${(totalSaved / 1024).toFixed(2)} KB so far.`);
        res.writeHead(204);
        return res.end();
    }

    console.log(`📡 TUNNELING: ${url.hostname}`);

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

server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 H-ROUTER DASHBOARD LIVE`);
    console.log(`Watching your 6GB RAM for Data Savings...`);
});
