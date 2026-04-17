import hashlib
import secrets
import string

def create_secure_voucher():
    # 1. Generate a 12-digit random numeric PIN
    raw_pin = ''.join(secrets.choice(string.digits) for _ in range(12))
    
    # 2. Generate a unique Salt for this specific transaction
    salt = secrets.token_hex(16)
    
    # 3. Create a SHA-256 Hash for the Huma-ledger
    # We never store the 'raw_pin' on the blockchain.
    ledger_hash = hashlib.sha256((raw_pin + salt).encode()).hexdigest()
    
    print("--- HUMA VOUCHER GENERATED ---")
    print(f"FOR USER (Raw PIN): {raw_pin}")
    print(f"FOR LEDGER (Secure Hash): {ledger_hash}")
    print(f"SALT (Stored with Hash): {salt}")
    print("------------------------------")
    print("INSTRUCTION: Only the Hash and Salt are written to Ubuntu.")

if __name__ == "__main__":
    create_secure_voucher()
