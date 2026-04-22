import hashlib
import base58

def to_huma_address(eth_address):
    # Remove '0x' if present
    clean_eth = eth_address.lower().replace("0x", "")
    # Add your Sovereign Version Byte (Huma Prefix logic)
    payload = b'\x08\x88' + bytes.fromhex(clean_eth)
    # Double SHA256 Checksum for security
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    # Encode to the Huma Format
    return "huma_" + base58.b58encode(payload + checksum).decode()

def from_huma_address(huma_addr):
    # Decodes back to 0x for the machine layer
    raw = base58.b58decode(huma_addr.replace("huma_", ""))
    return "0x" + raw[2:-4].hex()

if __name__ == "__main__":
    test_eth = "0x0000000000000000000000000000000000000888"
    print(f"Branded Address: {to_huma_address(test_eth)}")
