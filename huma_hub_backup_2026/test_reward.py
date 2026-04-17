huma_supply = 700000000
utility_reserve = 140000000 # 20% reserved for rewards
daily_emission = utility_reserve / (365 * 10) # 10-year distribution

def calculate_rig_reward(uptime_percent, blocks_processed):
    base = (daily_emission / 888) # Per Rig share share of the 888 Rigs
    return base * (uptime_percent / 100) * (1 + (blocks_processed / 10000))

# Example: A high-performing Rig in Nigeria (+234)
reward = calculate_rig_reward(99.9, 15000)
print(f"💰 RIG REWARD: {reward:.4f} HUMA generated for this cycle.")
