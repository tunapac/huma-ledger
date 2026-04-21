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
        print("-" * 30)

    def special_move(self):
        if self.role == "Architect":
            print(f"✨ {self.name} activates: LEDGER STRIKE!")
            print(">>> Validating block... Damage: 45 HP")
        elif self.role == "Pioneer":
            print(f"⚡ {self.name} activates: PI-REVOLUTION!")
            print(">>> Speed blitz... Damage: 50 HP")

# Initialize characters
architect = Kombatant("Tunapac", "Architect", 120, 80)
pioneer = Kombatant("Pioneer-001", "Pioneer", 90, 110)

print("INITIALIZING COMBAT PROTOCOL...")
architect.display_stats()
architect.special_move()
print("\n")
pioneer.display_stats()
pioneer.special_move()
