import segno
import time
import hashlib

def create_dqa_payload(asset_id):
    secret_salt = "HUMA_SOVEREIGN_KEY_5B"
    timestamp = str(int(time.time()))
    raw_data = f"{asset_id}:{timestamp}"
    
    # Create a unique hash
    token = hashlib.sha256((raw_data + secret_salt).encode()).hexdigest()
    return f"huma://verify/{asset_id}/{token}"

# Generate the QR code
if __name__ == "__main__":
    asset = "ASSET_12345"
    payload = create_dqa_payload(asset)
    qr = segno.make_qr(payload)
    qr.save("huma_auth_code.png", scale=10)
    print(f"QR Code generated for {asset}")
    print(f"Payload: {payload}")
