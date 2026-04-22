class HumaAgentSystem15:
    def __init__(self):
        self.commission_rate = 0.15  # 15% Agent Fee
        self.tax_rate = 0.00888      # 0.888% Sovereign Tax

    def process_ticket(self, stake_amount):
        agent_cut = stake_amount * self.commission_rate
        treasury_tax = stake_amount * self.tax_rate
        net_house = stake_amount - (agent_cut + treasury_tax)
        
        print(f"\n[AGENT-COMMISSION]: 15% Locked.")
        print(f"STAKE: {stake_amount:.2f}")
        print(f"AGENT EARNINGS: {agent_cut:.2f}")
        print(f"HUMA TREASURY: {treasury_tax:.2f}")
        return agent_cut

if __name__ == "__main__":
    agent = HumaAgentSystem15()
    # Example: If a player stakes 2000 Naira/HUMA
    agent.process_ticket(2000)
