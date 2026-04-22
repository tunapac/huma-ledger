class HumaAgentSystem:
    def __init__(self):
        self.base_commission = 0.10  # 10%
        self.win_bonus = 0.02       # 2%

    def calculate_payout(self, total_sales, total_winnings_paid):
        commission = total_sales * self.base_commission
        bonus = total_winnings_paid * self.win_bonus
        total_agent_pay = commission + bonus
        
        print(f"\n[AGENT-VOUCHER]: Settlement Processing...")
        print(f"SALES COMM (10%): {commission:.2f} $HUMA")
        print(f"WIN BONUS (2%): {bonus:.2f} $HUMA")
        print(f"TOTAL PAYOUT: {total_agent_pay:.2f} $HUMA")
        return total_agent_pay

if __name__ == "__main__":
    agent = HumaAgentSystem()
    # If agent sells 50,000 HUMA and pays out 10,000 in wins
    agent.calculate_payout(50000, 10000)
