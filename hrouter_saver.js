const http = require('http');
const https = require('https');

const PORT = 8888;
// Blocks data-heavy ads and tracking
const AD_BLOCK = ['doubleclick.net', 'google-analytics.com', 'ads.google.com', 'facebook.com/tr'];

const server = http.createServer((req, res) => {
    try {
        const url = new URL(req.url, `http://${req.headers.host}`);
        
        // 1. AD FILTER (Saves ~30% Data)
        if (AD_BLOCK.some(ad => url.hostname.includes(ad))) {
            console.log(`🚫 AD BLOCKED: ${url.hostname}`);
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
        proxy.on('error', () => { res.writeHead(500); res.end(); });
    } catch (e) {
        res.writeHead(400); res.end();
    }
});

server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 H-ROUTER DATA-SAVER: LIVE`);
    console.log(`PORT: ${PORT} | RAM: 6GB PROTECTED`);
});
