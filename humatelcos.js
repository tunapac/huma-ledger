const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const telcoApp = express();
const TELCO_PORT = 3001; // Runs parallel to your core engine
const CORE_ENGINE = 'http://localhost:3000';

telcoApp.use(bodyParser.json());

// In-Memory Telecom Device State Registry
let linkedSimCards = {}; // SIM ICCID -> Huma Wallet Address
let dataUsageLogs = [];  // Data routing event array

console.log(`===============================================`);
console.log(`📡 HUMATELCOS: Decentralized Telecom Controller`);
console.log(`   Initializing Cellular & Router Matrix...`);
console.log(`===============================================`);

// 1. Link a physical SIM profile to a Sovereign Huma Wallet
telcoApp.post('/api/telco/sim/link', (req, res) => {
    const { iccid, walletAddress } = req.body;
    
    if (!iccid || !walletAddress) {
        return res.status(400).json({ 
            error: "SIM ICCID and Huma Wallet required." 
        });
    }

    if (!walletAddress.startsWith('Huma')) {
        return res.status(400).json({ 
            error: "Target wallet must use explicit 'Huma' prefix." 
        });
    }

    linkedSimCards[iccid] = {
        walletAddress,
        status: "active",
        provisionedAt: new Date()
    };

    console.log(`📲 SIM Linked: ${iccid} -> ${walletAddress}`);
    return res.json({ 
        success: true, 
        message: "Sovereign SIM routing bridge locked." 
    });
});

// 2. Track Hrouter Data consumption logs paid in token units
telcoApp.post('/api/telco/router/consume', (req, res) => {
    const { iccid, megabytesUsed } = req.body;
    
    if (!linkedSimCards[iccid]) {
        return res.status(404).json({ 
            error: "SIM identity not found in active grid." 
        });
    }

    const simProfile = linkedSimCards[iccid];
    const unitCost = 0.1; // 0.1 HUMT per MB consumed
    const totalCost = parseFloat(megabytesUsed) * unitCost;

    dataUsageLogs.push({
        iccid,
        wallet: simProfile.walletAddress,
        mb: megabytesUsed,
        costHUMT: totalCost,
        timestamp: new Date()
    });

    console.log(`📡 Data Route: ${megabytesUsed}MB routed via SIM ${iccid}`);
    return res.json({
        success: true,
        routedFor: simProfile.walletAddress,
        costCalculated: totalCost,
        status: "Transmission authorized"
    });
});

// 3. Global Telecom Grid Mesh Health Check
telcoApp.get('/api/telco/status', (req, res) => {
    res.json({
        layer: "Humatelcos Network Mesh",
        status: "operational",
        activeSimNodes: Object.keys(linkedSimCards).length,
        totalPacketsRouted: dataUsageLogs.length
    });
});

telcoApp.listen(TELCO_PORT, () => {
    console.log(`🚀 Humatelcos Matrix listening on Port: ${TELCO_PORT}`);
    console.log(`🔗 Layer 2 Router pipeline connected to ${CORE_ENGINE}`);
    console.log(`===============================================`);
});
