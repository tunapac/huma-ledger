import hashlib
import random
import time

class HumaNetworkIssuer:
    def __init__(self):
        self.secret_seed = "OGUN_HUB_8G_RESONANCE_2026"

    def generate_huma_voucher(self, value_type="8G_DATA"):
        # Create a unique serial based on time and a random seed
        raw_string = f"{time.time()}-{random.random()}-{self.secret_seed}"
        # Create a secure hash and take the first 16 characters
        secure_pin = hashlib.sha256(raw_string.encode()).hexdigest()[:16].upper()
        
        # Format for readability: XXXX-XXXX-XXXX-XXXX
        formatted_pin = "-".join([secure_pin[i:i+4] for i in range(0, 16, 4)])
        return {
            "type": value_type,
            "pin": formatted_pin,
            "serial": f"HUMA-{random.randint(100000, 999999)}"
        }

if __name__ == "__main__":
    issuer = HumaNetworkIssuer()
    print("--- GENERATING SOVEREIGN HUMA-VOUCHERS ---")
    for _ in range(5):
        v = issuer.generate_huma_voucher()
        print(f"TYPE: {v['type']} | PIN: {v['pin']} | {v['serial']}")
