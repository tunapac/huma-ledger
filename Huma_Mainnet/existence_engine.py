import time
import hashlib
import random
from datetime import datetime

# --- TUNAPAC HUMANLEDGER: PERMANENT LEDGER PROTOCOL ---
huma_supply = 700000000.0
atom_supply = 0.0
tx_finality = 3
ledger_file = "ledger_history.txt"

def log_to_ledger(message):
    with open(ledger_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def generate_txid(phase):
    seed = f"Tunapac_{phase}_{time.time()}_{random.random()}"
    return hashlib.sha256(seed.encode()).hexdigest()

def execute_signed_vesting():
    global huma_supply, atom_supply
    
    # --- PHASE 1: FIRST 5 HUMA ---
    txid_1 = generate_txid("PHASE_1")
    huma_supply -= 5
    atom_supply += 500000000
    msg1 = f"BURN: 5 HUMA | MINT: 500M ATOM | TXID: {txid_1}"
    log_to_ledger(msg1)
    
    print("\n🛰️  +888 HROUTER GRID: PHASE 1 LOGGED")
    print(f"🆔  TXID: {txid_1}")
    
    # --- 3-SECOND SPACE ---
    time.sleep(tx_finality) 
    
    # --- PHASE 2: SECOND 5 HUMA ---
    txid_2 = generate_txid("PHASE_2")
    huma_supply -= 5
    atom_supply += 500000000
    msg2 = f"BURN: 5 HUMA | MINT: 500M ATOM | TXID: {txid_2}"
    log_to_ledger(msg2)
    
    print("\n🛰️  +888 HROUTER GRID: PHASE 2 LOGGED")
    print(f"🆔  TXID: {txid_2}")
    
    final_status = f"STATUS: HUMA REMAINING: {huma_supply:,.0f} | ATOM TOTAL: {atom_supply:,.0f}"
    log_to_ledger(final_status)
    print(f"\n✅  SUCCESS: 1,000,000,000 ATOM VESTED")

# --- INITIAL LAUNCH ---
print("--- TUNAPAC HUMANLEDGER HUB: PERMANENT LEDGER ONLINE ---")
execute_signed_vesting()
