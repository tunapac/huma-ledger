# Humanledger Multi-Account & Merchant Logic
# Rule 1: Individual max 2 accounts.
# Rule 2: Company/Merchant requires Employment Verification.

class AccountValidator:
    def __init__(self):
        self.member_accounts = {} # Maps Bio-ID to account list
        self.merchant_accounts = {}

    def create_individual_account(self, biometric_id):
        """Allows exactly 2 accounts per unique human biometric."""
        current_accounts = self.member_accounts.get(biometric_id, [])
        if len(current_accounts) < 2:
            new_account = f"Huma-IND-{len(current_accounts) + 1}"
            current_accounts.append(new_account)
            self.member_accounts[biometric_id] = current_accounts
            print(f"Account Created: {new_account} for Biometric ID {biometric_id}")
            return True
        else:
            print("ALERT: Individual limit of 2 accounts reached.")
            return False

    def create_merchant_account(self, merchant_name, employee_list):
        """Allows companies to create accounts based on employment status."""
        print(f"Initializing Merchant Account for: {merchant_name}")
        print(f"Verifying {len(employee_list)} employees for payroll...")
        self.merchant_accounts[merchant_name] = employee_list
        print(f"Merchant {merchant_name} is now ACTIVE on the 6G Grid.")

# Execution
validator = AccountValidator()
# Individual Test
validator.create_individual_account("BIO-DNA-001")
validator.create_individual_account("BIO-DNA-001")
validator.create_individual_account("BIO-DNA-001") # Should fail

# Merchant Test
validator.create_merchant_account("Tuna-Corp", ["EMP-01", "EMP-02"])
