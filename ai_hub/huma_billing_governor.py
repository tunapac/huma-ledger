# Humanledger Membership Billing Governor
# Logic: Member UBI Deduction vs. External Premium Pricing

class HumaBilling:
    def __init__(self):
        self.member_rate = 0.0001  # Atom per minute/MB
        self.external_rate = 0.05   # Higher rate for non-members
        self.monthly_ubi = 10000

    def process_usage(self, member_id, usage_units, is_member=True):
        """Calculates and deducts cost based on membership status."""
        if is_member:
            cost = usage_units * self.member_rate
            remaining_ubi = self.monthly_ubi - cost
            print(f"Member {member_id}: Usage deducted from UBI.")
            print(f"Cost: {cost} Atom | Remaining Monthly UBI: {remaining_ubi} Atom")
        else:
            cost = usage_units * self.external_rate
            print(f"External User: Premium Rate Applied.")
            print(f"Total Cost: {cost} (Payment required via External Gateway)")

# Testing the Tiered Economy
billing = HumaBilling()
# Scenario A: Registered Member using the 100M Rig Mesh
billing.process_usage("Huma-TUNAPAC-001", 500, is_member=True)
# Scenario B: Outside user accessing the grid
billing.process_usage("Guest-999", 500, is_member=False)
