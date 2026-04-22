class HumaRecruitment:
    def __init__(self):
        self.target_agents = 1000
        self.active_agents = []

    def onboard_agent(self, name, location, huma_id):
        agent_profile = {
            "name": name,
            "location": location,
            "huma_id": huma_id,
            "commission": 0.15,
            "status": "ACTIVE"
        }
        self.active_agents.append(agent_profile)
        print(f"\n[ONBOARDING]: Agent {name} ({huma_id}) at {location} is LIVE.")
        print(f"[REWARD]: 15% Commission Protocol Activated.")
        return agent_profile

if __name__ == "__main__":
    hub = HumaRecruitment()
    hub.onboard_agent("Tunapac_Agent_001", "Lagos_Market_Node", "huma_A888_001")
