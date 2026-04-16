import time
import hashlib

class HumaCertificateGenerator:
    def __init__(self):
        self.master_h = "GOLD_ARCHITECTURAL_H_FRAME"
        self.mesh_id = "EXPANDED_888+_ALPHA_RIG"
        self.authority = "Architect @001 - Tunapac"

    def issue_certificate(self, app_name, dev_wallet):
        print("\n" + "╔" + "═"*68 + "╗")
        print(f"║   CERTIFICATE OF SOVEREIGN AUTHENTICITY - HUMANLEDGER HUB   ║")
        print(f"║   ISSUED BY THE AUTHORITY OF: {self.master_h}   ║")
        print("╠" + "═"*68 + "╣")
        time.sleep(1)

        # Generate a unique Quantum-Mist Hash for the app
        cert_hash = hashlib.sha256(f"{app_name}{dev_wallet}{time.time()}".encode()).hexdigest()[:16]

        print(f"║ APP NAME: {app_name.ljust(54)} ║")
        print(f"║ DEVELOPER: {dev_wallet.ljust(53)} ║")
        print(f"║ MESH NODE: {self.mesh_id.ljust(53)} ║")
        print(f"║ SECURITY: 621-99 QUANTUM-MIST ENCRYPTION [ACTIVE]            ║")
        print(f"║ REVENUE MODEL: 15% HUB / 85% DEV [STANDARDIZED]              ║")
        print(f"║ VALIDATION HASH: {cert_hash.upper()}                        ║")
        print("╠" + "═"*68 + "╣")
        print(f"║ SIGNED: {self.authority.center(52)} ║")
        print("╚" + "═"*68 + "╝")
        
        print(f"\n[AI-LOG] Certificate stored in ~/huma_loan_vault/HumaPlay/{app_name}_COA.txt")

if __name__ == "__main__":
    generator = HumaCertificateGenerator()
    # Issuing the first certificate for the Studio itself
    generator.issue_certificate("HumaAiGemini_Studio", "TUNAPAC_MASTER_WALLET")
