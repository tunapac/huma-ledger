import time

class HumaMintSystem:
    def __init__(self):
        self.huma_price_usd = 0.10  # Initial Price: 1 $HUMA = $0.10
        self.domain_price_usd = 20.00 # $20 per .huma domain
        self.treasury_vault = 700000000

    def calculate_ejection(self, fiat_amount, currency):
        # In production, we'd hook into a real-time FX Oracle
        huma_to_mint = fiat_amount / self.huma_price_usd
        return huma_to_mint

    def process_mint(self, domain_name, fiat_paid, currency, user_wallet):
        huma_value = self.calculate_ejection(fiat_paid, currency)
        
        # Logic: Fiat is received -> Huma is "ejected" (transferred) to user
        print(f"--- MINTING LOG ---")
        print(f"Domain: {domain_name}.huma")
        print(f"Payment: {fiat_paid} {currency}")
        print(f"Ejection: {huma_value} $HUMA sent to {user_wallet}")
        print(f"Status: Domain anchored to Humanledger Root.")
        
        return {"status": "SUCCESS", "huma_ejected": huma_value}

if __name__ == "__main__":
    mounter = HumaMintSystem()
    mounter.process_mint("tunapac-store", 20.00, "USD", "0xHUMA_ARCH_1")
