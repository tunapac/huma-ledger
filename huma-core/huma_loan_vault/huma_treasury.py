import time

class HumaTreasury:
    def __init__(self):
        self.total_huma = 700000000
        self.classic_per_huma = 100000000 # 100M Classics = 1 Huma
        self.vault_atom = 0
        self.vault_classics = 0

    def record_fee(self, app_name, fee_atom):
        # 1 ATOM = 1 Classic in our value peg
        self.vault_atom += fee_atom
        new_classics = fee_atom 
        self.vault_classics += new_classics

        print(f"\n[TREASURY] Transaction Logged: {app_name}")
        print(f" -> Received: {fee_atom} ATOM")
        print(f" -> Minted: {new_classics} Classics (¢)")
        print(f" -> CURRENT VAULT BALANCE: {self.vault_classics} ¢")

    def show_status(self):
        print("\n" + "="*50)
        print("     OFFICIAL HUMA-LEDGER TREASURY STATUS")
        print("="*50)
        print(f"TOTAL HUMACOIN SUPPLY: {self.total_huma:,} HUMA")
        print(f"TOTAL CLASSIC SUPPLY:  {self.total_huma * self.classic_per_huma:,} ¢")
        print(f"TREASURY ATOM RESERVE: {self.vault_atom} ATOM")
        print(f"TREASURY CLASSIC REVENUE: {self.vault_classics} ¢")
        print("="*50)

if __name__ == "__main__":
    treasury = HumaTreasury()
    # Recording the 10 ATOM fee for each of your 11 apps (Creation + Logo = 20 ATOM each)
    for i in range(1, 12):
        treasury.record_fee(f"HumaApp_{i:02d}", 20)
    
    treasury.show_status()
