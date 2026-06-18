const readline = require('readline');
const axios = require('axios');

const CORE_ENGINE = 'http://localhost:3000';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

console.log(`===============================================`);
console.log(`🌐 HUMABROWSER: Sovereign Web3 Terminal Client`);
console.log(`   Connected Engine: ${CORE_ENGINE}`);
console.log(`===============================================`);

function launchBrowserPrompt() {
    rl.question('HumaBrowser:// ', async (input) => {
        let domain = input.trim().toLowerCase();
        
        if (domain === 'exit') {
            rl.close();
            return;
        }

        if (!domain) {
            launchBrowserPrompt();
            return;
        }

        try {
            console.log(`🔍 Resolving ${domain} via P2P DNS...`);
            
            // Query local core engine for Web3 DNS record
            const dnsRes = await axios.get(
                `${CORE_ENGINE}/api/dns/resolve/${domain}`
            );
            
            const targetAddress = dnsRes.data.address;
            console.log(`✅ Resolved! Target Address: ${targetAddress}`);
            console.log(`📥 Fetching decentralized payload...`);
            
            // Simulate reading the frontend mock from index.html 
            const siteRes = await axios.get(`${CORE_ENGINE}/index.html`);
            
            console.log(`\n--- [ RENDERED CONTENT: ${domain} ] ---`);
            console.log(siteRes.data);
            console.log(`-----------------------------------------\n`);
            
        } catch (err) {
            console.log(`❌ Operational Error:`);
            if (err.response) {
                if (err.response.status === 404) {
                    console.log(`   [404] Connected to Engine, but index.html payload is missing.`);
                } else {
                    console.log(`   Engine returned status code: ${err.response.status}`);
                }
            } else {
                console.log(`   Network Connection Failed: ${err.message}`);
            }
        }
                console.log(`   Domain not found in .Huma TDL.`);
            } else {
                console.log(`   ${err.message}`);
            }
        }
        launchBrowserPrompt();
    });
}

launchBrowserPrompt();
