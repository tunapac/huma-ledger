import os
from huma_translator import to_huma_address

def display_wallet(supply):
    # HARDCORE MEMORY LOCK: The Admin Identity is huma_branded
    # We no longer reference the 0x000... legacy string in the display logic.
    
    # This is your unique Sovereign Admin Hash derived for the Huma Mesh
    admin_core_hash = "8888888888888888888888888888888888888888"
    admin_huma_id = to_huma_address(admin_core_hash)

    os.system('clear')
    print("====================================================")
    print("           TUNAPAC HUMANLEDGER HUB - WALLET          ")
    print("====================================================")
    print(f" SOVEREIGN ID: {admin_huma_id}") 
    print(f" RANK: TIER 2 SOVEREIGN GLOBAL ADMINISTRATOR")
    print("----------------------------------------------------")
    print(f" [!] TOTAL HUMA SUPPLY: {supply:,}")
    print(f" [!] NETWORK STATUS: LIVE (8G MESH)")
    print(f" [!] PROTOCOL: +888 SOVEREIGN IDENTITY")
    print("====================================================")

if __name__ == "__main__":
    display_wallet(699950000)
