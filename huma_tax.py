class HumaTreasury:
    def __init__(self):
        self.tax_rate = 0.00888
        self.treasury_address = "huma_G888SovereignAdmin" # Your locked ID

    def calculate_tax(self, amount):
        tax_amount = amount * self.tax_rate
        net_amount = amount - tax_amount
        print(f"\n[TAX-ENGINE]: 0.888% Protocol Fee applied.")
        print(f"[REVENUE]: {tax_amount:.4f} sent to {self.treasury_address}")
        return net_amount

if __name__ == "__main__":
    tax = HumaTreasury()
    tax.calculate_tax(1000)
