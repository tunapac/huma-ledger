class Huma8GRigMesh:
    def __init__(self):
        self.generation = "8G"
        self.protocol = "+888 Hyperbridge"
        self.huma_per_gb = 0.5  # Reward for Volume
        self.huma_per_hour = 1.2 # Reward for Uptime
        self.rigs = {}

    def calculate_rewards(self, rig_id, gb_processed, hours_active):
        # Dual-Mining Logic
        volume_reward = gb_processed * self.huma_per_gb
        uptime_reward = hours_active * self.huma_per_hour
        total_reward = volume_reward + uptime_reward
        
        self.rigs[rig_id] = {
            "volume_mined": volume_reward,
            "uptime_mined": uptime_reward,
            "total": total_reward
        }
        return self.rigs[rig_id]

if __name__ == "__main__":
    mesh = Huma8GRigMesh()
    # Simulation: Rig active for 24 hours moving 100GB of 8G traffic
    result = mesh.calculate_rewards("RIG-PORT-HARCOURT-01", 100, 24)
    print(f"8G Mesh Rewards: {result['total']} HUMA")
