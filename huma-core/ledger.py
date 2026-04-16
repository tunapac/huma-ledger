class HumaSovereignLedger:
    def __init__(self):
        self.total_supply = 700_000_000
        self.repayment_vault = 0.0
        self.service_cut_percentage = 0.15
        self.facility_limit = 250_000_000.0

    def process_transaction(self, sender, receiver, amount):
        cut_amount = amount * self.service_cut_percentage
        net_transfer = amount - cut_amount
        self.repayment_vault += cut_amount
        print(f'\n[ TRANSACTION SUCCESS ]')
        print(f'Total Amount: {amount} HUMA')
        print(f'Repayment Cut (15%): {cut_amount} HUMA')
        print(f'Net to Recipient: {net_transfer} HUMA')
        progress = (self.repayment_vault / self.facility_limit) * 100
        print(f'Facility Progress: {progress:.8f}%')

ledger = HumaSovereignLedger()
ledger.process_transaction("Architect_001", "Global_Exchange", 1000000.0)
