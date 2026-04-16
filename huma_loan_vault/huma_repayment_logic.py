class HumaROI:
    def __init__(self):
        self.loan_amount = 250000000
        self.members = 1000000
        self.hub_cut = 0.15 # The Standardized 15%
        self.avg_monthly_spend = 10 # 10 Atom (Å) per member

    def calculate_repayment(self):
        # Monthly Revenue from the 15% cut on member spending
        monthly_revenue = self.members * self.avg_monthly_spend * self.hub_cut
        annual_revenue = monthly_revenue * 12
        years_to_repay = self.loan_amount / annual_revenue

        print("\n" + "═"*70)
        print("   TUNAPAC HUMANLEDGER HUB | REPAYMENT FORECAST")
        print("═"*70)
        print(f" -> ACTIVE MEMBERS: {self.members:,}")
        print(f" -> MONTHLY REVENUE (15% CUT): ${monthly_revenue:,.2f}")
        print(f" -> ANNUAL REVENUE: ${annual_revenue:,.2f}")
        print("-" * 70)
        print(f" PROJECTED FULL REPAYMENT: {years_to_repay:.2f} YEARS")
        print("═"*70)
        print(" STATUS: BANK-READY SUSTAINABILITY MODEL.")

if __name__ == "__main__":
    forecast = HumaROI()
    forecast.calculate_repayment()
