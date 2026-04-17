import hashlib
import time
import random

class HumaSovereignBanking:
    def __init__(self, address):
        self.address = address # Must start with Huma-
        self.balance = 700.0
        self.staked_amount = 0.0

    # --- HUMACARD: Virtual Chip Logic ---
    def generate_virtual_card(self):
        # Generates a non-EVM virtual card linked to Huma- address
        card_num = f"8888-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"
        cvv = str(random.randint(100, 999))
        expiry = "08/29" # Sovereign Launch Era
        return {"card_number": card_num, "cvv": cvv, "expiry": expiry, "type": "HumaCard Virtual"}

    # --- STAKING DASHBOARD: Proof-of-Stake Logic ---
    def stake_huma(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.staked_amount += amount
            reward_rate = 0.0888 # 8.88% Protocol +888 APY
            return f"STAKED: {amount} HUMA. Expected Annual Reward: {amount * reward_rate} HUMA"
        return "Insufficient Balance"

if __name__ == "__main__":
    bank = HumaSovereignBanking("Huma-7F3A2B9C")
    
    # 1. Issue Virtual Chip Card
    card = bank.generate_virtual_card()
    print(f"--- HUMACARD ISSUED ---")
    print(f"Number: {card['card_number']} | CVV: {card['cvv']}")
    
    # 2. Start Staking
    print(f"\n--- STAKING ACTIVATED ---")
    print(bank.stake_huma(500))
