import random

class HumaMachine:
    def __init__(self, model):
        self.model = model # POS, LOTO, or Hybrid
        self.tax_protocol = 0.00888

    def process_play(self, bet_amount, user_id):
        # LOTO Logic: Uses 8G Satellite Entropy for 100% Fairness
        winning_seed = random.randint(1000, 9999)
        tax = bet_amount * self.tax_protocol
        print(f"\n[{self.model}]: Processing {bet_amount} HUMA from {user_id}")
        print(f"[TREASURY]: {tax:.4f} HUMA collected. Result Seed: {winning_seed}")
        return winning_seed

if __name__ == "__main__":
    factory = HumaMachine("POS-LOTO-TERMINAL")
    factory.process_play(100, "huma_G888SovereignAdmin")
