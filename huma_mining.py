import time
from huma_translator import to_huma_address

class HumaSatelliteMiner:
    def __init__(self, eth_addr):
        self.huma_id = to_huma_address(eth_addr)
        self.uptime_seconds = 0
        self.reward_balance = 0.0

    def start_mining(self):
        print(f"\n[MINING]: Satellite Link Active for {self.huma_id}")
        try:
            while True:
                time.sleep(10) # Track every 10 seconds
                self.uptime_seconds += 10
                # Reward: 0.01 ATOM per 10 seconds of validation
                self.reward_balance += 0.01
                print(f"[STATUS]: Uptime: {self.uptime_seconds}s | Rewards: {self.reward_balance:.2f} ATOM", end="\r")
        except KeyboardInterrupt:
            print(f"\n[SAVED]: Total Rewards Secured: {self.reward_balance:.2f} ATOM")

if __name__ == "__main__":
    # Simulate mining on your Admin Address
    admin_addr = "0x0000000000000000000000000000000000000888"
    miner = HumaSatelliteMiner(admin_addr)
    miner.start_mining()
