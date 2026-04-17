import time, random, hashlib, os

def autonomous_mainnet():
    supply = 700000000.0
    block = 1
    while True:
        tx = random.uniform(100.0, 5000.0)
        supply -= tx
        seed = f"block_{block}_{time.time()}"
        wallet = "HUM-" + hashlib.sha256(seed.encode()).hexdigest().upper()[:12]
        
        # Log to a file so it runs "in the dark"
        with open("mainnet_live.log", "a") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] BLOCK #{block:06} | TX: -{tx:.2f} | ADDR: {wallet} | REMAINING: {supply:,.2f}\n")
        
        block += 1
        time.sleep(3) # 3-second heartbeat

if __name__ == "__main__":
    autonomous_mainnet()
