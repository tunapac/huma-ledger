class HumaDNSBridge:
    def __init__(self, sovereign_dns):
        self.sovereign_dns = sovereign_dns
        self.web2_gateway = "huma.link"

    def get_traditional_url(self, huma_name):
        # Converts huma://tunapac to tunapac.huma.link
        if huma_name in self.sovereign_dns.registry:
            return f"https://{huma_name}.{self.web2_gateway}"
        return "Address not found in Sovereign Registry"

    def handle_web2_request(self, web2_url):
        # Logic for the huma.link server to fetch blockchain data
        name = web2_url.split('.')[0]
        blockchain_address = self.sovereign_dns.resolve(name)
        return f"Redirecting to Huma Blockchain Address: {blockchain_address}"

if __name__ == "__main__":
    from huma_dns import HumaDNS
    core_dns = HumaDNS()
    core_dns.register_name("tunapac", "HUMA_ARCHITECT_001")
    
    bridge = HumaDNSBridge(core_dns)
    print(f"\n[BRIDGE ACTIVE]: {bridge.get_traditional_url('tunapac')}")
