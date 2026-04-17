import time
import random

def live_feed():
    actions = ["MINTED", "TRANSFERRED", "STAKED", "LOCKED"]
    while True:
        amount = random.randint(10, 5000)
        wallet = f"0x{random.randint(1000, 9999)}...{random.randint(1000, 9999)}"
        print(f"\033[1;32m[TXN] {amount} HUMA {random.choice(actions)} | TO: {wallet} | GENESIS: OK\033[0m")
        time.sleep(random.uniform(1.5, 4.0))

if __name__ == "__main__":
    live_feed()
