import subprocess
import datetime

# --- GENESIS CONFIG ---
PROJECT = "Tunapac Humanledger Hub"
TOTAL_SUPPLY = 700000000
ATOM_VAL = 100000000
REF_REWARD_ATOM = 0.5 

def send_h_mail(email, member_id, amount_huma):
    subject = f"REWARD CONFIRMED: {PROJECT}"
    body = f"Greetings Member {member_id},\n\nYour 0.5 Atom ({amount_huma:.10f} HUMANLEDGER) reward is minted."
    cmd = f'echo "{body}" | mail -s "{subject}" {email}'
    try:
        subprocess.run(cmd, shell=True)
        print(f"[✔] H-MAILER: Reward alert sent to {email}")
    except:
        print("[!] H-MAILER: Mail queued")

def process_reference(member_id, email):
    reward_huma = REF_REWARD_ATOM / ATOM_VAL
    print(f"\n--- {PROJECT} ---")
    print(f"[*] Processing Reference for {member_id}...")
    print(f"[+] Minting {REF_REWARD_ATOM} Atom...")
    
    with open("vault_ledger.txt", "a") as f:
        f.write(f"ID:{member_id} | REWARD:{reward_huma:.10f} HUMA | UNIT:0.5 ATOM\n")
    
    send_h_mail(email, member_id, reward_huma)
    print(f"[SUCCESS] Ledger updated for {member_id}\n")

# TEST THE SYSTEM
process_reference("TUNAPAC_FOUNDER", "admin@humanledger.hub")
