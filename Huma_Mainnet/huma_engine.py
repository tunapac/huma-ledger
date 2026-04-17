import time, random, os

def run_mainnet():
    supply = 700000000.0
    block = 1
    print("\033[1;32m[SYSTEM] MAINNET ENGINE STARTED. LOGGING TO 'live_blocks.log'\033[0m")
    
    while True:
        # Simulate 3-second block transaction
        tx = random.uniform(50.0, 1000.0)
        supply -= tx
        
        # Log to file (Save your RAM/Screen)
        with open("live_blocks.log", "a") as f:
            log_entry = f"Block #{block:06} | Time: {time.strftime('%H:%M:%S')} | Supply: {supply:,.2f} HUMA\n"
            f.write(log_entry)
        
        block += 1
        time.sleep(3)

if __name__ == "__main__":
    run_mainnet()
