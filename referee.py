class HumaLotoReferee:
    def __init__(self):
        self.tax_protocol = 0.00888

    def process_result(self, player_bet, draw_win, draw_mac):
        # The Player's own prediction vs the Random Draw
        win_hits = set(player_bet).intersection(draw_win)
        mac_hits = set(player_bet).intersection(draw_mac)

        # Checking for the "Direct 2" (1 from Win, 1 from Machine)
        if len(win_hits) >= 1 and len(mac_hits) >= 1:
            return "WINNER: DIRECT 2"
        return "NO MATCH: TRY AGAIN"

# Test the logic
if __name__ == "__main__":
    ref = HumaLotoReferee()
    # Example: Player played 8 and 88. 8 is in Win, 88 is in Machine.
    result = ref.process_result([8, 88], [8, 10, 20, 30, 40], [88, 50, 60, 70, 80])
    print(f"\n[GAME RESULT]: {result}")
