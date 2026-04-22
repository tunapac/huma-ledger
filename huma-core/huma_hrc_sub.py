class HRC_Subscription_Standard:
    def __init__(self, developer_id, project_name):
        self.dev = developer_id
        self.project = project_name
        self.sub_plans = {}  # Store plans: {plan_id: price}

    def create_plan(self, plan_id, price):
        self.sub_plans[plan_id] = price
        print(f"\n[HRC-SUB]: New Plan '{plan_id}' created for {self.project}")
        print(f" > Price Set: {price} $HUMA")

    def request_authorization(self, user_id, plan_id):
        price = self.sub_plans.get(plan_id)
        if price:
            print(f"\n[HRC-AUTH]: Merchant {self.dev} requesting {price} $HUMA from User {user_id}")
            return True
        print("[HRC-ERROR]: Plan not found.")
        return False

# Testing the Library logic
if __name__ == "__main__":
    # Simulate a Developer launching a Streaming App
    huma_stream = HRC_Subscription_Standard("dev_888", "HumaStream_Global")
    huma_stream.create_plan("PREMIUM_MONTHLY", 50)
    huma_stream.request_authorization("user_voter_1", "PREMIUM_MONTHLY")
