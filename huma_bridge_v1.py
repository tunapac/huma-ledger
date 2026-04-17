import time

class HumaBridge:
    def __init__(self):
        self.supported_coins = ["HUMA", "ATOM_STABLE"]
        self.fiat_channels = ["NGN", "USD", "EUR", "GBP"]
        self.protocol_fee = 0.00888  # 0.888% instead of 30%

    def process_payment(self, amount, currency, user_address):
        print(f"\n[BRIDGE]: Detecting Payment via {currency}...")
        time.sleep(1)
        
        if currency in self.supported_coins:
            print(f"[DIRECT]: Processing {amount} {currency} to {user_address}")
        elif currency in self.fiat_channels:
            print(f"[FIAT-INJECTION]: Converting {currency} {amount} into HUMA Liquidity...")
            # Logic to "Inject" fiat into the Huma Coin value
            print(f"[STRENGTHENING]: Huma Coin Market Cap increased by {amount} {currency}")
        
        print(f"[SETTLED]: Transaction Complete. Protocol Fee: {amount * self.protocol_fee}")
        return True

if __name__ == "__main__":
    bridge = HumaBridge()
    # Test 1: Huma Payment
    bridge.process_payment(100, "HUMA", "Huma-7F3A2B9C")
    # Test 2: Fiat Injection
    bridge.process_payment(5000, "NGN", "Huma-D8E1F2G3")
