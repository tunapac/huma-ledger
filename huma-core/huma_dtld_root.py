import hashlib
import time

class HumaRootDNS:
    def __init__(self):
        # This is the "Sovereign Root Zone"
        # It replaces the ICANN root database
        self.root_zone = {
            ".huma": {"owner": "Tunapac", "created": 2026},
            ".ledger": {"owner": "Treasury", "created": 2026},
            ".8g": {"owner": "Network", "created": 2026}
        }
        self.records = {} # The actual map of huma:// address to IP/Wallet

    def register_on_chain(self, domain, tld, target_ip, owner_sig):
        """
        Registers a name directly onto the Humanledger.
        Example: register_on_chain('bank', '.huma', '10.104.191.165', 'SIG_01')
        """
        if tld not in self.root_zone:
            return "[ERROR]: Unauthorized TLD. Only .huma, .ledger, .8g are Root-Active."
        
        full_domain = f"{domain}{tld}"
        if full_domain in self.records:
            return "[ERROR]: Domain already minted on-chain."

        # Create a "Huma-Record" Hash (Proof of Ownership)
        record_hash = hashlib.sha256(f"{full_domain}{owner_sig}".encode()).hexdigest()
        
        self.records[full_domain] = {
            "target": target_ip,
            "hash": record_hash,
            "timestamp": time.time()
        }
        return f"[SUCCESS]: {full_domain} is now live on the Sovereign Root."

    def resolve(self, full_domain):
        """The Oracle function that translates human names to network addresses"""
        record = self.records.get(full_domain)
        if record:
            return record["target"]
        return "[404]: Domain not found in Sovereign Root."

if __name__ == "__main__":
    huma_dns = HumaRootDNS()
    # Minting the first official domain on our own TLD
    print(huma_dns.register_on_chain("hub", ".huma", "10.104.191.165", "TUNAPAC_KEY_001"))
    print(f"Resolving hub.huma... Direction: {huma_dns.resolve('hub.huma')}")
