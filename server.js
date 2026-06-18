const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const crypto = require('crypto');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// ====================================================
//  GLOBAL STATE & CONFIGURATIONS
// ====================================================
const FIXED_SUPPLY_HUMT = 600000000;
let web3DnsRegistry = {};   
let userHumtBalances = {};   
let walletToUserMap = {};    

// P2P Swarm Nodes & Web3 RPC Infrastructure Targets
let peerNodes = []; 
const WEB3_RPC_PROVIDER = "https://rpc.ankr.com/eth"; 

// ====================================================
//  MODULE A: DECENTRALIZED P2P SWARM NETWORK BRIDGE
// ====================================================

// Broadcast updated DNS routes to all connected P2P peers
async function broadcastToP2PSwarm(endpoint, payload) {
    console.log(`📡 Swarm: Broadcasting payload to peers...`);
    peerNodes.forEach(async (peer) => {
        try {
            await axios.post(`${peer}${endpoint}`, payload, { timeout: 2000 });
            console.log(`✅ Swarm: Synced successfully with peer: ${peer}`);
        } catch (err) {
            console.log(`❌ Swarm: Peer ${peer} unreachable. Line dropped.`);
        }
    });
}

// Receive incoming DNS state sync requests from other Web3 nodes
app.post('/api/p2p/sync-dns', (req, res) => {
    const { domain, walletAddress } = req.body;
    if (domain && walletAddress) {
        web3DnsRegistry[domain] = walletAddress;
        console.log(`🔗 P2P Sync: Bound ${domain} -> ${walletAddress}`);
        return res.json({ success: true, message: "State synced" });
    }
    return res.status(400).json({ error: "Malformed P2P packet" });
});

// Join a new peer node into your local cluster matrix
app.post('/api/p2p/connect-node', (req, res) => {
    const { peerUrl } = req.body;
    if (!peerUrl) return res.status(400).json({ error: "Missing peerUrl" });
    
    if (!peerNodes.includes(peerUrl)) {
        peerNodes.push(peerUrl);
    }
    return res.json({ success: true, activePeers: peerNodes });
});

// ====================================================
//  MODULE B: BLOCKCHAIN GLOBAL RPC INTERACTION LAYER
// ====================================================

// Fetch live block data or state from global decentralized mainnets
app.get('/api/web3/global-block', async (req, res) => {
    try {
        const rpcPayload = {
            jsonrpc: "2.0",
            method: "eth_blockNumber",
            params: [],
            id: 1
        };
        
        const response = await axios.post(WEB3_RPC_PROVIDER, rpcPayload);
        const hexBlock = response.data.result;
        const decimalBlock = parseInt(hexBlock, 16);
        
        return res.json({
            success: true,
            networkProvider: "Ankr Web3 RPC Gateway",
            currentGlobalBlock: decimalBlock,
            hex: hexBlock
        });
    } catch (error) {
        return res.status(500).json({ 
            error: "Failed to pull live Web3 state",
            details: error.message 
        });
    }
});

// ====================================================
//  CORE ACCOUNT & SOVEREIGN DNS ENGINE
// ====================================================

function generateCustomHumaWallet() {
    const privateKey = crypto.randomBytes(32).toString('hex');
    const hash = crypto.createHash('sha256').update(privateKey).digest('hex');
    const walletAddress = "Huma" + hash.substring(0, 30);
    return {
        privateKey: `pv_key_${privateKey.substring(0, 24)}`,
        walletAddress: walletAddress
    };
}

function isValidHumaAddress(address) {
    if (!address || typeof address !== 'string') return false;
    return address.startsWith('Huma') && address.length >= 15;
}

app.post('/api/dns/register', async (req, res) => {
    try {
        let { domain, walletAddress } = req.body;
        if (!domain || !walletAddress) {
            return res.status(400).json({ error: "Missing fields" });
        }
        domain = domain.trim().toLowerCase();
        if (!domain.endsWith('.huma')) domain = domain + '.huma';
        
        if (!isValidHumaAddress(walletAddress)) {
            return res.status(400).json({ error: "Invalid address prefix" });
        }
        
        web3DnsRegistry[domain] = walletAddress;

        // P2P Action: Instantly broadcast this registration across the network
        await broadcastToP2PSwarm('/api/p2p/sync-dns', { domain, walletAddress });

        return res.json({ success: true, domain, resolvedTo: walletAddress });
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
});

app.get('/api/dns/resolve/:domain', (req, res) => {
    let domain = req.params.domain.trim().toLowerCase();
    if (!domain.endsWith('.huma')) domain = domain + '.huma';
    const address = web3DnsRegistry[domain];
    if (!address) return res.status(404).json({ error: "Domain not found" });
    return res.json({ success: true, domain, address });
});

app.post('/api/wallet/generate', (req, res) => {
    try {
        const { username } = req.body;
        if (!username) return res.status(400).json({ error: "Username required" });
        const credentials = generateCustomHumaWallet();
        walletToUserMap[credentials.walletAddress] = username;
        userHumtBalances[credentials.walletAddress] = 0;
        return res.json({
            success: true,
            username,
            address: credentials.walletAddress,
            privateKey: credentials.privateKey
        });
    } catch (error) {
        return res.status(500).json({ error: error.message });
    }
});

app.get('/api/ecosystem/status', (req, res) => {
    res.json({
        status: "active",
        tdlProtocol: ".Huma Web3 DNS Swarm Active",
        totalSupplyHUMT: FIXED_SUPPLY_HUMT,
        connectedP2PPeers: peerNodes.length,
        totalRegisteredDomains: Object.keys(web3DnsRegistry).length
    });
});

app.listen(PORT, () => {
    console.log(`===============================================`);
    console.log(`🚀 Tunapac Humanledger Global Web3 Engine`);
    console.log(`📡 Port: ${PORT} | Active Network Swarm Bridges`);
    console.log(`🔗 Connected to External Web3 RPC Networks`);
    console.log(`===============================================`);
});
