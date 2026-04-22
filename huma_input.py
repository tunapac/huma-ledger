class GameController:
    def __init__(self):
        self.move_left = False
        self.move_right = False
        self.action_punch = False

    def touch_down(self, x, y):
        # Simulated screen zones for an Android phone
        if x < 100:
            self.move_left = True
            print("⬅️ MOVEMENT: Walking Left")
        elif x > 200:
            self.move_right = True
            print("➡️ MOVEMENT: Walking Right")
        elif 100 < x < 200:
            self.action_punch = True
            print("👊 ATTACK: High Punch!")

# Test the Input Logic
controller = GameController()
print("--- TESTING VIRTUAL PAD ---")
controller.touch_down(50, 0)   # Simulating a touch on the left side
controller.touch_down(150, 0)  # Simulating a touch in the center
controller.touch_down(250, 0)  # Simulating a touch on the right side
