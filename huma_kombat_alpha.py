import pygame

class HumanityFighter:
    def __init__(self, name):
        self.name = name
        self.state = "IDLE"
        self.position = 0
        self.hp = 100
        print(f"--- 🛡️ {self.name} ENTERING THE ARENA ---")

    def update(self, input_command):
        if input_command == "LEFT":
            self.state = "WALKING_LEFT"
            self.position -= 5
        elif input_command == "RIGHT":
            self.state = "WALKING_RIGHT"
            self.position += 5
        elif input_command == "PUNCH":
            self.state = "ATTACKING"
        else:
            self.state = "IDLE"
        
        print(f"STATE: {self.state:15} | POSITION: {self.position:3} | HP: {self.hp}")

# --- THE VIRTUAL PAD LOGIC ---
def simulate_mobile_touch(x_coord):
    # This simulates your phone screen width (0 to 300)
    if x_coord < 100: return "LEFT"
    if x_coord > 200: return "RIGHT"
    return "PUNCH"

# --- RUNNING THE COMBAT TEST ---
player = HumanityFighter("Tunapac")
touches = [50, 50, 250, 150] # Left, Left, Right, Punch

for finger_tap in touches:
    command = simulate_mobile_touch(finger_tap)
    player.update(command)
