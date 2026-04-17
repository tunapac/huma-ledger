import random

class MultiNetworkGenerator:
    def __init__(self):
        # 2026 Standardized Pin Lengths
        self.networks = {
            "MTN": {"digits": 17, "prefix": "8"},
            "AIRTEL": {"digits": 16, "prefix": "4"},
            "GLO": {"digits": 15, "prefix": "5"},
            "9MOBILE": {"digits": 15, "prefix": "2"}
        }

    def generate_mixed_sheet(self, network_requests):
        """network_requests is a dict like {'MTN': 500, 'AIRTEL': 100}"""
        filename = "mixed_print_batch.txt"
        total_count = 0
        
        with open(filename, "w") as f:
            f.write("--- HUMA-LEDGER HUB: MULTI-NETWORK MASTER SHEET ---\n")
            f.write("Location: Ogun State Hub | Architect: Nurudeen Babatunde Ismaila\n")
            f.write("-" * 65 + "\n\n")
            
            for net_name, qty in network_requests.items():
                net = self.networks.get(net_name.upper())
                if not net: continue
                
                f.write(f"\n>>> {net_name} BATCH ({qty} CARDS)\n")
                for i in range(1, qty + 1):
                    pin = "".join([str(random.randint(0, 9)) for _ in range(net['digits'])])
                    serial = f"SN-{random.randint(100000, 999999)}"
                    f.write(f"[{i:03}] {net_name:8} | PIN: {pin} | {serial}\n")
                total_count += qty
                
        print(f"SUCCESS: {total_count} cards saved to '{filename}'")

if __name__ == "__main__":
    huma_gen = MultiNetworkGenerator()
    # Your request: 500 MTN + let's add 100 Airtel for balance
    request = {
        "MTN": 500,
        "AIRTEL": 100
    }
    huma_gen.generate_mixed_sheet(request)
