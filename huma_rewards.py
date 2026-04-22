def calculate_huma_reward(result, difficulty="Normal"):
    # The 700,000,000 supply logic
    base_reward = 10.0
    
    if result == "WIN":
        multiplier = 1.5
        status = "FATALITY! Victory Achieved."
    else:
        multiplier = 0.5
        status = "DEFEAT! Try again, Pioneer."
        
    total_earned = base_reward * multiplier
    print(f"--- 🛡️ HUMANITY LEDGER SETTLEMENT ---")
    print(f"RESULT: {status}")
    print(f"REWARD: {total_earned} HUMA Coins")
    print(f"NETWORK: Huma-Blockchain Mainnet")
    print("-" * 36)

# Test for the Architect
calculate_huma_reward("WIN")
