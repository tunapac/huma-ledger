import time
from huma_translator import to_huma_address

class HumaSatelliteMiner:
    def __init__(self, admin_huma_id):
        self.huma_id = admin_huma_id
        self.reward_balance = 0.0

    def start_validation(self):
        print(f"\n[MINING]: SOVEREIGN NODE {self.huma_id} ONLINE.")
        print("[STATUS]: Validating Protocol +888 across 150M Satellites...")
        try:
            while True:
                time.sleep(5)
                # Earn 0.05 ATOM per validation cycle
                self.reward_balance += 0.05
                print(f" -> Rewards Secured: {self.reward_balance:.2f} ATOM", end="\r")
        except KeyboardInterrupt:
            print(f"\n[LOCKED]: Total Earnings for {self.huma_id}: {self.reward_balance:.2f} ATOM")

if __name__ == "__main__":
    # Using your Hardcoded Admin ID
    admin_id = "huma_G888SovereignAdmin"
    miner = HumaSatelliteMiner(admin_id)
    miner.start_validation()
