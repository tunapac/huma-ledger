import json

def set_market_rates():
    # 2026 MARKET DATA (Reference)
    # 1 HUMA target value: $0.10 (Theoretical Founder's Peg)
    # Nigeria Avg 1GB: ~$0.32 | USA Avg 1GB: ~$6.00
    
    rates = {
        "NIGERIA": {
            "country_code": "+234",
            "huma_per_gb": 3.0,  # ~ $0.30/GB (Competitive with local N637/GB)
            "min_purchase": 0.5  # GB
        },
        "USA": {
            "country_code": "+1",
            "huma_per_gb": 50.0, # ~ $5.00/GB (Cheaper than $6.00 avg)
            "min_purchase": 1.0  # GB
        }
    }
    
    print("🌐 HUMA-LEDGER: GLOBAL MARKETPLACE INITIALIZED")
    print("---------------------------------------------")
    for region, data in rates.items():
        print(f"📍 REGION: {region} ({data['country_code']})")
        print(f"📊 RATE:   {data['huma_per_gb']} HUMA per 1GB")
        print(f"💎 VALUE:  ~${data['huma_per_gb'] * 0.10:.2f} USD equivalent")
        print("-" * 30)

    with open('market_rates.json', 'w') as f:
        json.dump(rates, f, indent=4)
    print("✅ Rates anchored to market_rates.json")

if __name__ == "__main__":
    set_market_rates()
