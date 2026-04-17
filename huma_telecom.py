import time
import sys

def print_888_grid():
    grid = """
\033[1;36m    ####################################################
    #  +888  +888  +888  |  HUMANLEDGER HUB NODE 0.1   #
    #  +888  +888  +888  |  SUPPLY: 700,000,000 HUMA   #
    #  +888  +888  +888  |  ARCHITECT: TUNAPAC         #
    ####################################################\033[0m
    """
    print(grid)

def h_sim_activation():
    print("\n\033[1;34m[H-TELECOM] INITIALIZING DEPIN PROTOCOL...")
    time.sleep(1)
    print("[eSIM] H-SIM DETECTED: tunapac4real247.hum.huma")
    print("\033[1;32m[STATUS] H-SIM MOBILE: ACTIVE (5G DECENTRALIZED)\033[0m")

def h_router_status():
    print("\n\033[1;33m[H-ROUTER] MOBILE WIRELESS HUB CHECK...")
    time.sleep(1)
    print("[MESH] BROADCASTING GENESIS SIGNAL...")
    print("\033[1;32m[STATUS] HROUTER: ONLINE | BANDWIDTH: 1.2 Gbps\033[0m")

def telecom_menu():
    print_888_grid()
    print("--- HUMANLEDGER TELECOM HUB (GENESIS LIVE) ---")
    print("1. Activate H-SIM & Data Reward")
    print("2. Check HRouter Status")
    print("3. Exit")
    
    choice = input("\nSelect Command: ")
    
    if choice == "1":
        h_sim_activation()
        print("\033[1;32m[BONUS] 5GB FREE DATA CREDITED TO H-SIM.\033[0m")
    elif choice == "2":
        h_router_status()
    else:
        print("Closing Telecom Node...")

if __name__ == "__main__":
    telecom_menu()
