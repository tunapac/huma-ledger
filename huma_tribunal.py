import time

class HumaAILawTribunal:
    def __init__(self):
        self.tax_rate = 0.00888
        self.required_prefix = "huma_"

    def audit_project(self, project_name, wallet_id, tax_compliance):
        print(f"\n[TRIBUNAL]: Auditing '{project_name}'...")
        time.sleep(1.5)
        
        # Rule 1: Identity Check
        if not wallet_id.startswith(self.required_prefix):
            print(f"[VERDICT]: GUILTY. Legacy address detected. Access Denied.")
            return False
            
        # Rule 2: Tax Compliance Check
        if tax_compliance < self.tax_rate:
            print(f"[VERDICT]: GUILTY. Tax evasion detected. Freezing Assets.")
            return False

        print(f"[VERDICT]: COMPLIANT. Project authorized for 8G Mesh.")
        return True

if __name__ == "__main__":
    tribunal = HumaAILawTribunal()
    # Test a compliant project
    tribunal.audit_project("HumaSwap", "huma_G888SovereignAdmin", 0.00888)
