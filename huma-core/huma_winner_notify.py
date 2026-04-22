class HumaWinnerNotifier:
    def __init__(self):
        self.winners_ledger = {}

    def validate_1_to_90(self, numbers):
        # The Architect's Rule: Strictly 1 to 90
        for num in numbers:
            if num < 1 or num > 90:
                raise ValueError(f"[SOVEREIGN-ERROR]: Invalid ball {num} detected! The rule is strictly 1-90.")
        return True

    def scan_for_winners(self, draw_results, subscribed_tickets):
        # draw_results: [ [5 win balls], [5 machine balls] ]
        self.validate_1_to_90(draw_results[0])
        self.validate_1_to_90(draw_results[1])
        
        for user_id, ticket in subscribed_tickets.items():
            self.validate_1_to_90(ticket) # Validate player's ticket too
            
            win_hits = set(ticket).intersection(draw_results[0])
            mac_hits = set(ticket).intersection(draw_results[1])
            
            # Direct 2 Win Logic
            if len(win_hits) >= 1 and len(mac_hits) >= 1:
                self.winners_ledger[user_id] = "DIRECT 2 WINNER"
                self.trigger_alert(user_id, "YOU WON! Your Direct 2 hit is ready.")

    def trigger_alert(self, user_id, message):
        print(f"\n[PUSH-NOTIFICATION] -> {user_id}: {message}")

if __name__ == "__main__":
    notify = HumaWinnerNotifier()
    # Corrected Test Data: Strictly within 1-90
    results = [[8, 10, 20, 30, 40], [88, 55, 66, 77, 90]]
    tickets = {"user_voter_1": [8, 88]}
    
    print("\n--- VALIDATING SATURDAY NATIONAL RESULTS ---")
    try:
        notify.scan_for_winners(results, tickets)
        print("[CONSENSUS]: Draw verified. All balls strictly between 1 and 90.")
    except ValueError as e:
        print(e)
