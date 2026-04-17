import json

def load_ledger():
    with open("huma_ledger.json", "r") as f: return json.load(f)

def run_hub():
    data = load_ledger()
    sym = data['designed_symbols']
    
    print("\n" + "═"*60)
    print(f"   TUNAPAC HUMANLEDGER HUB - WEB 3.0 & AI EVOLUTION")
    print(f"   PROTOCOL: QFS 20022 | SECURITY: QUANTUM-RESISTANT")
    print("═"*60)
    print(f" [1] Ⱨ-BOOK SOCIAL   : Access Decentralized Feed")
    print(f" [2] NFT MINTING     : Mint Asset (Fee: 100 {sym['CLASSIC']})")
    print(f" [3] AI ASSISTANT    : Gemini-5-4 Agentic Mode")
    print(f" [4] QFS TERMINAL    : Execute ISO 20022 Payment")
    print("-" * 60)
    
    choice = input("Select Hub Function > ")
    
    if choice == "3":
        print("\n[AI] Huma Assistant: 'Awaiting your command, Architect. How can I optimize the 888+ Grid today?'")
    elif choice == "2":
        print(f"\n[SYSTEM] Initializing Quantum-Resistant Minting for {sym['HUMA']}...")
    else:
        print("\n[STATUS] Connecting to Huma Book Mesh...")

if __name__ == "__main__":
    run_hub()
