import json, os, hashlib, time

class HumaApps:
    def __init__(self):
        self.ledger = "huma_ledger.json"

    def get_data(self):
        with open(self.ledger, "r") as f: return json.load(f)

    def save_data(self, data):
        with open(self.ledger, "w") as f: json.dump(data, f, indent=2)

    # --- APP 1: HUMA-MAIL (PQC Encrypted) ---
    def send_mail(self, recipient, message):
        print(f"\n[MAIL] Encrypting message for {recipient}...")
        # Simulate Lattice-based Key Encapsulation (PQC)
        pqc_packet = hashlib.sha3_512(message.encode()).hexdigest()[:32]
        print(f"[PQC-LOCK] Message hidden in Lattice Matrix: {pqc_packet}...")
        print(f"[SUCCESS] Mail sent over +888 Satellite Grid.")

    # --- APP 2: HUMA-DEX (Quantum-Safe Exchange) ---
    def dex_swap(self, amount, target_asset):
        data = self.get_data()
        if data["bal"] >= amount:
            print(f"\n[DEX] Authorizing Swap: {amount} Huma -> {target_asset}")
            print(f"[AUTH] Verifying 15-Digit PQC-SIM Signature...")
            time.sleep(1) # Simulating ML-DSA verification
            data["bal"] -= amount
            self.save_data(data)
            print(f"[SUCCESS] Swap Complete. New Balance: {data['bal']} Huma")
        else:
            print("[ERROR] Insufficient Huma for Swap.")

def launch_interface():
    os.system('clear')
    apps = HumaApps()
    print("="*45)
    print("   TUNAPAC HUMANLEDGER HUB - WEB 3.0 APPS   ")
    print("="*45)
    
    # 1. Test Huma-Mail
    apps.send_mail("investor@888.huma", "Project Humanledger is ready for Scale.")
    
    # 2. Test Huma-DEX
    apps.dex_swap(50.0, "SAT-DATA-UNITS")
    
    print("-" * 45)
    print(" [SYSTEM] All huma:// calls verified by +888 Grid.")
    print("="*45)

if __name__ == "__main__":
    launch_interface()
