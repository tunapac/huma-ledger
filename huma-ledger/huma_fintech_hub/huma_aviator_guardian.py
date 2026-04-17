# TUNAPAC 8G HUMANLEDGER: HUMA-AVIATOR AI GUARDIAN V
# Architect: Nurudeen Babatunde Ismaila
# Master Node: 001 | Family Node: 004

import random
import time

class HumaAviatorV:
    def __init__(self):
        self.master_ids = ["001", "004"]
        self.outsider_cap = 2000.0
        self.master_target = 100000.0
        self.supported_currencies = ["EUR", "GBP", "HUMA", "BTC", "ETH"]

    def process_stake(self, user_id, amount, currency):
        if currency.upper() not in self.supported_currencies:
            return "REJECTED: Use EUR, GBP, or HUMA."

        # THE AI GUARDIAN MONITORING LOOP
        print(f"[AI GUARD] Monitoring Stake: {amount} {currency} from User {user_id}")
        
        # Generate the "True" Flight Potential
        true_flight = round(random.uniform(1.0, 150000.0), 2)

        if user_id in self.master_ids:
            # MASTER LOGIC: The plane is forced to reach for the 100,000x peak
            result = max(true_flight, self.master_target)
            status = "ALPHA_PRIORITY: LAST_OUT_SECURED"
        else:
            # OUTSIDER LOGIC: Hard ceiling at 2,000x
            result = min(true_flight, self.outsider_cap)
            status = "CAPPED_BY_HUB"

        return {"User": user_id, "Payout": f"{result}x", "Status": status}

if __name__ == "__main__":
    game = HumaAviatorV()
    print("--- ✈️ HUMA-AVIATOR AI GUARDIAN V: ONLINE ---")
    print("--- POOL CURRENCY: EUR / GBP / HUMA COIN ---")
    
    # Simulation
    print(f"Outsider Stake (EUR): {game.process_stake('GUEST_99', 50, 'EUR')}")
    print(f"Master Stake (HUMA): {game.process_stake('001', 1000, 'HUMA')}")
