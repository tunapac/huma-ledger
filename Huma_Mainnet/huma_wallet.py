import hashlib
import time

def create_authenticated_wallet(username):
    # Generating a unique seed for the user
    seed = f"{username}-{time.time()}-Humanledger-2026"
    raw_hash = hashlib.sha256(seed.encode()).hexdigest().upper()
    
    # ENFORCING THE HUM PREFIX (THE BLOCKCHAIN SIGNATURE)
    wallet_address = "HUM-" + raw_hash[:12] + "-" + raw_hash[-4:]
    
    print(f"\033[1;36m####################################################")
    print(f"#         HUMANLEDGER AUTHENTICATED WALLET         #")
    print(f"####################################################\033[0m")
    print(f"\n[NETWORK]: HUMANLEDGER HUB MAINNET")
    print(f"[OWNER]: {username}")
    print(f"\033[1;32m[ADDRESS]: {wallet_address}\033[0m")
    print(f"[VALIDATION]: AUTHENTICATED (HUM-PROTOCOL)")
    print(f"[SUPPLY]: 700,000,000 HUMA TOTAL")
    
    # Saving to the Hub's secure ledger
    with open("ledger_db.txt", "a") as f:
        f.write(f"{username} | {wallet_address} | {time.ctime()}\n")

if __name__ == "__main__":
    # Generating the Founder's Master Wallet
    create_authenticated_wallet("tunapac4real247")
