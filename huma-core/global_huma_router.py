# TUNAPAC 8G HUMANLEDGER: TOP 10 SIMULATION
# Architect: Nurudeen Babatunde Ismaila

def simulate_global_call(country, duration):
    codes = {"USA": "+1", "CHINA": "+86", "GERMANY": "+49", "INDIA": "+91", "JAPAN": "+81"}
    rate = 5 # 5 Cents (Atom Stable)
    code = codes.get(country.upper(), "+??")
    cost = duration * rate
    return f"ROUTE: {code} | COST: {cost}¢ ({cost/100} HMD)"

if __name__ == "__main__":
    print("--- 8G HUB SIMULATION: TOP ECONOMIES ---")
    for nation in ["USA", "China", "India"]:
        print(simulate_global_call(nation, 10))
