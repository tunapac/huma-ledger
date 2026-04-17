from huma_translator import to_huma_address

class HumaHackathon:
    def __init__(self):
        self.prize_pool = 1000000  # 1M HUMA for the first Hackathon
        self.admin_id = "huma_G888SovereignAdmin"

    def reward_dev(self, dev_huma_id, amount):
        if not dev_huma_id.startswith("huma_"):
            return "[REJECTED]: Invalid Address Format. Huma Prefix Required."
        
        self.prize_pool -= amount
        print(f"\n[HACKATHON]: Prize of {amount} HUMA sent to {dev_huma_id}")
        print(f"[REMAINING POOL]: {self.prize_pool} HUMA")
        return "SUCCESS"

if __name__ == "__main__":
    hub = HumaHackathon()
    hub.reward_dev("huma_DevNodeAlpha999", 50000)
