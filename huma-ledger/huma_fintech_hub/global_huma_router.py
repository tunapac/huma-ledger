# TUNAPAC 8G HUMANLEDGER: GLOBAL ROUTING ENGINE
# Currency: Atom Stable (HMD) & Classic Cent (¢)
# Architect: Nurudeen Babatunde Ismaila

class GlobalRouter:
    def __init__(self):
        # Global Dialing Codes for the Launch
        self.dial_codes = {
            "NIGERIA": "+234", "USA": "+1", "UK": "+44",
            "GHANA": "+233", "CHINA": "+86", "INDIA": "+91"
        }
        self.rate_per_min = 0.05  # Standard Rate: 5¢ (HMD Cents)

    def route_call(self, country_name, duration_mins):
        code = self.dial_codes.get(country_name.upper())
        if not code:
            return "Country Code Not Initialized"
        
        # Calculate cost in classic cents (¢)
        total_cents = duration_mins * (self.rate_per_min * 100)
        total_hmd = (total_cents / 100)
        
        return {
            "destination": country_name,
            "dialing_code": code,
            "duration": f"{duration_mins} min",
            "cost_cents": f"{total_cents}¢",
            "cost_hmd": f"{total_hmd} HMD"
        }

if __name__ == "__main__":
    router = GlobalRouter()
    # Test a call from the Ogun Hub to the UK
    call = router.route_call("UK", 10)
    print(f"--- 8G GLOBAL CALL INITIALIZED ---")
    print(f"TARGET: {call['destination']} ({call['dialing_code']})")
    print(f"BILLING: {call['cost_cents']} (Atom Stable Standard)")
