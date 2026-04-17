import time
import random

class HumaDrone:
    def __init__(self, drone_id):
        self.id = drone_id
        self.status = "GROUNDED"
        self.mesh_link = "OFFLINE"

    def initiate_flight(self):
        print(f"\n[DRONE-{self.id}]: PRE-FLIGHT CHECK...")
        time.sleep(1)
        self.status = "AIRBORNE"
        self.mesh_link = "ACTIVE (8G)"
        
        print(f"[DRONE-{self.id}]: TAKEOFF SUCCESSFUL.")
        print(f"[DRONE-{self.id}]: EXTENDING MESH VIA PROTOCOL +888...")
        
        # Simulate signal strength boost
        signal = random.randint(90, 100)
        print(f"[DRONE-{self.id}]: MESH SIGNAL STRENGTH: {signal}%")
        return "MISSION_ACTIVE"

if __name__ == "__main__":
    drone = HumaDrone("ALPHA-001")
    drone.initiate_flight()
