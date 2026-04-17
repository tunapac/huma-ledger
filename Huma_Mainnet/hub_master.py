import os, time, random, hashlib

def get_poy_id():
    # Unique ID based on your Redmi 14C hardware
    try:
        hw_id = os.popen("grep -i serial /proc/cpuinfo").read().strip()
        if not hw_id: hw_id = "REDMI-14C-NODE-ALPHA"
    except:
        hw_id = "OFFLINE-NODE-001"
    return hashlib.sha256(f"{hw_id}tunapac".encode()).hexdigest().upper()[:10]

def launch_dashboard():
    supply = 700000000.0
    blocks = 0
    poy = get_poy_id()
    start_time = time.time()
    
    while True:
        os.system('clear')
        uptime = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
        # Simulated mining deduction (3-second heartbeat)
        mined = random.uniform(5.5, 250.0)
        supply -= mined
        blocks += 1
        
        print("\033[1;34m┌──────────────────────────────────────────────────┐\033[0m")
        print("\033[1;32m│         TUNAPAC HUMANLEDGER HUB - MAINNET        │\033[0m")
        print("\033[1;34m├──────────────────────────────────────────────────┤\033[0m")
        print(f"\033[1;37m  ARCHITECT: TUNAPAC        NODE ID: {poy}\033[0m")
        print(f"\033[1;37m  UPTIME:    {uptime}       STATUS:  RUNNING\033[0m")
        print("\033[1;34m├──────────────────────────────────────────────────┤\033[0m")
        print(f"\033[1;33m  TOTAL HUMA SUPPLY:  {supply:,.2f}\033[0m")
        print(f"\033[1;36m  CURRENT BLOCK:      #{blocks:06}\033[0m")
        print(f"\033[1;32m  LATEST REWARD:      +{mined:.2f} HUMA\033[0m")
        print("\033[1;34m└──────────────────────────────────────────────────┘\033[0m")
        print("\033[1;30m[MINING ACTIVE - PRESS CTRL+C TO ENTER COMMANDS]\033[0m")
        
        # Log to the permanent registry
        with open("registry.log", "a") as f:
            f.write(f"{time.ctime()} | Block {blocks} | {supply} HUMA\n")
            
        time.sleep(3)

if __name__ == "__main__":
    launch_dashboard()
