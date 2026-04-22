import hashlib
import datetime

def generate_huma_id(username, wallet_address):
    # Create a unique hash
    raw_data = f"{username}-{wallet_address}-{datetime.datetime.now()}"
    huma_hash = hashlib.sha256(raw_data.encode()).hexdigest()[:16].upper()
    unique_id = f"HUMA-ID-{huma_hash}"
    
    # Clean print statements
    print("========================================")
    print("🛡️  HUMANITY LEDGER IDENTITY")
    print("========================================")
    print(f"ARCHITECT: {username}")
    print(f"SOVEREIGN ID: {unique_id}")
    print(f"NETWORK: Humanity Ledger")
    print(f"SUPPLY: 700,000,000 HUMA")
    print("========================================")
    print(f"✅ Identity Generated successfully.")
    print("========================================")

# Run it
generate_huma_id("Tunapac", "G-ARCHITECT-001")
+ 
