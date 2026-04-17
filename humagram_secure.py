from cryptography.fernet import Fernet
import time

class HumaSecureChat:
    def __init__(self):
        # In a real Tier 2 scenario, the key is derived from Biometric/Humanode AI
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_payload(self, message):
        token = self.cipher.encrypt(message.encode())
        print(f"\n[ENCRYPTING]: Applying Protocol +888 Shield...")
        return token

    def decrypt_payload(self, token):
        print(f"[DECRYPTING]: Verifying Sovereign Signature...")
        return self.cipher.decrypt(token).decode()

if __name__ == "__main__":
    chat = HumaSecureChat()
    secret = "Sovereign Command: Launch Satellites at 0900"
    
    encrypted = chat.encrypt_payload(secret)
    print(f"[ON-MESH]: {encrypted[:30]}... (Encrypted)")
    
    time.sleep(1)
    decrypted = chat.decrypt_payload(encrypted)
    print(f"[PRIVATE]: {decrypted}")
