class HumaDNS:
    def __init__(self):
        self.registry = {} # { "name": "wallet_address_or_hash" }
        self.reg_fee = 10.0 # 10 $HUMA for a .huma name

    def register_name(self, name, target_address):
        if name in self.registry:
            return "[DNS-ERROR]: Name already taken."
        
        # Split the fee: 0.888% Tax, rest to Hub
        tax = self.reg_fee * 0.00888
        self.registry[name] = target_address
        
        print(f"\n[HUMA-DNS]: '{name}' is now registered to {target_address}")
        print(f" > Protocol: huma://{name}")
        print(f" > Sovereign Tax Burned: {tax:.4f}")
        return True

    def resolve(self, name):
        target = self.registry.get(name)
        if target:
            print(f"[RESOLVING]: huma://{name} -> {target}")
            return target
        return "[DNS-ERROR]: Address not found."

if __name__ == "__main__":
    dns = HumaDNS()
    dns.register_name("tunapac", "HUMA_ARCHITECT_WALLET_001")
    dns.resolve("tunapac")
