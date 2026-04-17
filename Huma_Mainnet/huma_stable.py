import time, random, os

def silent_engine():
    supply = 700000000.0
    block = 1
    # We log to a file so the screen stays clean
    while True:
        tx = random.uniform(10.0, 500.0)
        supply -= tx
        with open("mainnet.log", "a") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] BLOCK #{block:06} | SUPPLY: {supply:,.2f} HUMA\n")
        block += 1
        time.sleep(3) # The 3-second heartbeat

if __name__ == "__main__":
    silent_engine()
