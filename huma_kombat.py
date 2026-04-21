class Kombatant:
    def __init__(self, name, role, health, power):
        self.name = name
        self.role = role
        self.health = health
        self.power = power

    def display_stats(self):
        print(f"--- 🛡️ {self.role}: {self.name} ---")
        print(f"HP:    {'❤️' * (self.health // 10)}")
        print(f"POWER: {'🔥' * (self.power // 10)}")
        print(f"STATUS: Ready for Kombat")
        print("-" * 30)

# 1. The Architect Class (High Tech/Defense)
architect = Kombatant("Tunapac", "Architect", 120, 80)

# 2. The Pioneer Class (High Speed/Attack)
pioneer = Kombatant("Pioneer-001", "Pioneer", 90, 110)

print("INITIALIZING CHARACTER DATA...")
architect.display_stats()
pioneer.display_stats()
