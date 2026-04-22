import time

class HumaOffRamp:
    def __init__(self):
        self.supported_fiat = ["NGN", "USD", "EUR"]
        self.conversion_fee = 0.00888

    def withdraw_fiat(self, amount_huma, currency, bank_details):
        print(f"\n[OFF-RAMP]: Initiating withdrawal of {amount_huma} HUMA to {currency}...")
        time.sleep(2)
        print(f"[LIQUIDITY]: Fetching {currency} from Sovereign Vault...")
        print(f"[TRANSFER]: Sending {currency} value to {bank_details['bank_name']}...")
        print(f"[STATUS]: Withdrawal Complete. Protocol Fee: {amount_huma * self.conversion_fee} HUMA")

if __name__ == "__main__":
    ramp = HumaOffRamp()
    bank_info = {"bank_name": "Sovereign Bank", "account": "0011223344"}
    ramp.withdraw_fiat(5000, "NGN", bank_info)
