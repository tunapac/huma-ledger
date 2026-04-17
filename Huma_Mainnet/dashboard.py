import os, time, random

def draw_dashboard():
    supply = 700000000.0
    blocks = 1
    start_time = time.time()
    
    while True:
        os.system('clear')
        elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))
        # Logic for 3-second block deduction
        tx_out = random.uniform(10.5, 450.0)
        supply -= tx_out
        
        print("\033[1;36m==================================================\033[0m")
        print("\033[1;32m      TUNAPAC HUMANLEDGER HUB - MAINNET V1.0      \033[0m")
        print("\033[1;36m==================================================\033[0m")
        print(f"  [STATUS]    \033[1;32mONLINE\033[0m          [UPTIME]   {elapsed}")
        print(f"  [HARDWARE]  REDMI 14C       [ARCHITECT] TUNAPAC")
        print(f"  [PROTOCOL]  HUM-3S          [POY-ID]    ACTIVE")
        print("\033[1;36m--------------------------------------------------\033[0m")
        print(f"  [TOTAL SUPPLY]     \033[1;33m{supply:,.2f} HUMA\033[0m")
        print(f"  [CURRENT BLOCK]    #{blocks:06}")
        print(f"  [LATEST TX]        -{tx_out:.2f} HUMA")
        print("\033[1;36m--------------------------------------------------\033[0m")
        print("  \033[1;30m[RUNNING AUTO-MINING... PRESS CTRL+C TO EXIT]\033[0m")
        
        # Log to file in background
        with open("registry.log", "a") as f:
            f.write(f"Block {blocks} | Supply {supply}\n")
            
        blocks += 1
        time.sleep(3) # The 3-second heartbeat

if __name__ == "__main__":
    draw_dashboard()
