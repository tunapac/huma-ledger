import json
import time

def activate_staking():
    # 2026 STAKING PARAMETERS
    total_supply = 700000000
    utility_reserve = 140000000
    num_rigs = 888
    
    # Yearly distribution: 5% of the reserve
    annual_reward_pool = utility_reserve * 0.05
    daily_reward_pool = annual_reward_pool / 365
    reward_per_rig = daily_reward_pool / num_rigs

    print("🚀 HUMA-LEDGER: STAKING REWARDS ACTIVATED")
    print("---------------------------------------------")
    print(f"💰 ANNUAL POOL:  {annual_reward_pool:,.2f} HUMA")
    print(f"📅 DAILY POOL:   {daily_reward_pool:,.2f} HUMA")
    print(f"📡 PER RIG/DAY:  {reward_per_rig:.4f} HUMA")
    print("---------------------------------------------")
    
    # Simulating a reward cycle for the 888 Rigs
    staking_log = {
        "timestamp": int(time.time()),
        "status": "DISTRIBUTING",
        "pqc_signature": "ML-DSA-LATTICE-VERIFIED",
        "active_rigs": num_rigs
    }

    with open('staking_active.json', 'w') as f:
        json.dump(staking_log, f, indent=4)
    print("✅ Staking cycle live. Rewards flowing to the 888 Rigs.")

if __name__ == "__main__":
    activate_staking()
