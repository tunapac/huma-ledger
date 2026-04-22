import datetime

class HumaAgentSystemV3:
    def __init__(self):
        self.agent_fee = 0.0025  # 0.25%
        self.sovereign_tax = 0.00888  # 0.888%
        
    def calculate_settlement(self, stake_fiat, currency):
        # Stake is received in Fiat but converted internally
        fee_amount = stake_fiat * self.agent_fee
        tax_amount = stake_fiat * self.sovereign_tax
        house_keep = stake_fiat - (fee_amount + tax_amount)
        
        print(f"\n[SETTLEMENT - {currency}]:")
        print(f" AGENT FEE (0.25%): {fee_amount:.4f}")
        print(f" SOVEREIGN TAX (0.888%): {tax_amount:.4f}")
        print(f" NET TO HUB: {house_keep:.4f}")
        return fee_amount

if __name__ == "__main__":
    agent_v3 = HumaAgentSystemV3()
    # If a player stakes 10,000 Naira on Monday Special
    agent_v3.calculate_settlement(10000, "NGN")
