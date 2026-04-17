import json
import subprocess
import datetime
import os

# --- UNIVERSAL CONFIG ---
PROJECT = "Tunapac Humanledger Hub"
TOTAL_SUPPLY = 700000000
REWARD_ATOM = 0.5
ATOM_UNIT = 100000000

def update_cloud_ledger(member_id):
    huma_val = REWARD_ATOM / ATOM_UNIT
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = {
        "id": member_id,
        "reward": f"{huma_val:.10f}",
        "unit": "0.5 Atom",
        "time": timestamp
    }

    # Load existing or start new
    ledger_file = 'ledger.json'
    if os.path.exists(ledger_file):
        with open(ledger_file, 'r') as f:
            data = json.load(f)
    else:
        data = []

    data.append(new_entry)

    # Save the JSON (Web-Ready)
    with open(ledger_file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"[✔] 0.5 Atom Minted for {member_id}")
    
    # AUTO-PUSH TO GITHUB (Syncing Android -> Mac/PC/iOS)
    subprocess.run("git add ledger.json && git commit -m 'Cloud Update' && git push origin main", shell=True)
    print("[🚀] Synced to Global Cloud")

# Test Run
update_cloud_ledger("FOUNDER_TUNAPAC")
