class HumaMarket:
    def __init__(self):
        self.listings = {
            "Satellite_Bandwidth": 50,
            "Mesh_Node_License": 500,
            "AI_Liveness_Cert": 10
        }

    def browse(self):
        print("\n=== HUMA SOVEREIGN MARKETPLACE ===")
        for item, price in self.listings.items():
            print(f" * {item}: {price} ATOM")
        print("===================================")

if __name__ == "__main__":
    market = HumaMarket()
    market.browse()
