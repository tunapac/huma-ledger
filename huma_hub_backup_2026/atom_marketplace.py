import json

def initialize_atom_market():
    # 2026 STABLE PRICING (Pegged 1 ATOm = $1.00 USD)
    # Competitive Global Rates for the Masses
    
    market_config = {
        "NIGERIA": {
            "country_code": "+234",
            "atom_per_gb": 0.35,  # $0.35 USD (Competitive local rate)
            "min_topup": 1.0      # 1 ATOm
        },
        "USA": {
            "country_code": "+1",
            "atom_per_gb": 5.50,  # $5.50 USD (Cheaper than major carriers)
            "min_topup": 5.0      # 5 ATOm
        }
    }
    
    print("🛰️ HUMA-LEDGER: ATOM STABLE MARKETPLACE LIVE")
    print("---------------------------------------------")
    for region, data in market_config.items():
        print(f"📍 {region} ({data['country_code']})")
        print(f"💎 DATA RATE: {data['atom_per_gb']} ATOm per 1GB")
        print(f"✅ STABLE PEG: 1 ATOm = 1.00 USD")
        print("-" * 30)

    with open('atom_rates.json', 'w') as f:
        json.dump(market_config, f, indent=4)
    print("✅ ATOm rates anchored to atom_rates.json")

if __name__ == "__main__":
    initialize_atom_market()
