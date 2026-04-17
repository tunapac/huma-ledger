# TUNAPAC 8G HUMANLEDGER: AVIATOR PRIORITY SHIELD
# Master: +234 621 99 000 001 (Nurudeen)
# Family: +234 621 99 000 004 (Boluwaji)

import random
import time

class PriorityShield:
    def __init__(self):
        self.master_id = "001"
        self.family_id = "004"
        self.max_outsider_multiplier = 10.0

    def calculate_result(self, user_id, stake):
        # Base multiplier for the round
        base_multiplier = round(random.uniform(1.0, 50.0), 2)
        
        # LOGIC 1: Outsider Cap
        if user_id not in [self.master_id, self.family_id]:
            result = min(base_multiplier, self.max_outsider_multiplier)
            user_type = "OUTSIDER (CAPPED)"
        
        # LOGIC 2: Architect's Last-Out (Priority Tier)
        else:
            # If the Master/Family stakes high, we push the multiplier to the limit
            result = base_multiplier + (stake * 0.1) if stake > 100 else base_multiplier
            user_type = "ARCHITECT (ALPHA PRIORITY)"

        return {"Type": user_type, "Result": f"{result}x", "Status": "LAST_OUT" if user_id == self.master_id else "SYNCED"}

if __name__ == "__main__":
    shield = PriorityShield()
    print("--- 🛰️ 8G AVIATOR SHIELD: ACTIVE ---")
    
    # Simulation: Outsider hits a huge 45x flight
    print(f"User Guest: {shield.calculate_result('999', 500)}")
    
    # Simulation: Architect Nurudeen stakes high
    print(f"Master 001: {shield.calculate_result('001', 1000)}")
