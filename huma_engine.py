import pygame

class RealAvatar:
    def __init__(self):
        # We define the 'box' for one 1992 sprite (approx 60x130 pixels)
        self.width = 60
        self.height = 130
        self.current_frame = 0
        print("--- 🛡️ HUMANITY LEDGER GAME ENGINE ---")
        print("STATUS: 1992 Sprite Sheet detected.")
    
    def get_frame_rect(self):
        # This logic 'slices' the sheet so the avatar can move
        # Moving 60 pixels to the right for each frame
        x = self.current_frame * self.width
        return (x, 0, self.width, self.height)

    def next_frame(self):
        self.current_frame = (self.current_frame + 1) % 10
        rect = self.get_frame_rect()
        print(f"ACTION: Clipping Sprite at coordinates: {rect}")

# Run the test
fighter = RealAvatar()
for i in range(3):
    fighter.next_frame()
