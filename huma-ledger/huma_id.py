import hashlib
import datetime

def generate_huma_id(username, wallet):
    timestamp = str(datetime.datetime.now())
    raw = f"{username}{wallet}{timestamp}"
    h_id = hashlib.sha256(raw.encode()).hexdigest()[:12].upper()
    
    print("-" * 30)
    print("🛡️  HUMA IDENTITY GEN")
    print("-" * 30)
    print(f"USER: {username}")
    print(f"ID:   HUMA-{h_id}")
    print(f"GOAL: Financial Freedom")
    print("-" * 30)

generate_huma_id("Tunapac", "G-ARCH-01")
