class HumaHardware:
    def __init__(self, device_type):
        self.device_type = device_type # POS, LOTO, or Hybrid
        self.prefix = "huma_term_"

    def process_transaction(self, amount, user_huma_id):
        tax = amount * 0.00888
        print(f"\n[{self.device_type} TERMINAL]: Processing...")
        print(f"[AUTH]: User {user_huma_id} verified via Biometric Link.")
        print(f"[TREASURY]: {tax:.4f} HUMA routed to Admin.")
        return True

if __name__ == "__main__":
    pos = HumaHardware("POS-LOTO-HYBRID")
    pos.process_transaction(5000, "huma_User777")
