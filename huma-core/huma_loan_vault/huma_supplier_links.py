class HumaSovereignSourcing:
    def __init__(self):
        self.master_h = "DOUBLE_STRIKE_GOLD_H_FRAME"
        self.suppliers = {
            "Mühlbauer": "https://www.muehlbauer.de",
            "Matica": "https://www.maticagroup.com",
            "Entrust": "https://www.entrust.com"
        }

    def verify_procurement_targets(self):
        print("\n" + "="*60)
        print(f" OFFICIAL SUPPLIER DIRECTORY | {self.master_h}")
        print("="*60)
        for name, link in self.suppliers.items():
            print(f" SUPPLIER: {name.ljust(15)} | PORTAL: {link}")
        print("="*60)
        print("INSTRUCTION: Contact 'Central Issuance' divisions for $250M Quotes.")

if __name__ == "__main__":
    sourcing = HumaSovereignSourcing()
    sourcing.verify_procurement_targets()
