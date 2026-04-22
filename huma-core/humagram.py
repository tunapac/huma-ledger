import socket
import threading

class HumaGram:
    def __init__(self, port):
        self.host = '0.0.0.0'
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

    def receive_messages(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n[RECEIVED]: {message}")
            except:
                break

    def start_chat(self):
        print(f"\n[HUMAGRAM]: Sovereign Node listening on port {self.port}...")
        while True:
            client, addr = self.socket.accept()
            print(f"[SYSTEM]: Secure link established with {addr}")
            threading.Thread(target=self.receive_messages, args=(client,)).start()

    def send_message(self, target_ip, target_port, msg):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, target_port))
        client.send(msg.encode('utf-8'))
        client.close()

if __name__ == "__main__":
    # In a real scenario, use your Node ID's Port
    messenger = HumaGram(8888)
    messenger.start_chat()
