import json

class HumaGram:
    """HumaGram: Decentralized Communication for the Humanledger Hub"""
    def __init__(self, sender_id):
        self.sender_id = sender_id
        self.outbox = []

    def send_mesh_message(self, receiver_id, content):
        message = {
            "from": self.sender_id,
            "to": receiver_id,
            "payload": content,
            "protocol": "+888-MESH",
            "fee_status": "Locked (8%)"
        }
        self.outbox.append(message)
        return f"Message routed to Mesh Node: {receiver_id}"

    def get_outbox(self):
        return json.dumps(self.outbox, indent=2)

if __name__ == "__main__":
    app = HumaGram("Tunapac")
    app.send_mesh_message("Atoshi-Lead", "The +888 Protocol is Operational.")
    print(app.get_outbox())+
