from huma_translator import to_huma_address

def display_wallet(supply):
    # The machine sees 0x, but Tunapac sees HUMA
    admin_eth = "0x0000000000000000000000000000000000000888"
    huma_addr = to_huma_address(admin_eth)

    print("====================================================")
    print("           TUNAPAC HUMANLEDGER HUB - WALLET          ")
    print("====================================================")
    print(f" ADDRESS: {huma_addr}") 
    print(f" RANK: TIER 2 SOVEREIGN GLOBAL ADMINISTRATOR")
    print("----------------------------------------------------")
    print(f" [!] TOTAL HUMA SUPPLY: {supply:,}")
    print("====================================================")

if __name__ == "__main__":
    display_wallet(699950000)
