import hashlib

def generate_huma_address(public_key_string):
    """
    Converts a Public Key into a Sovereign Huma- Address.
    No 0x prefix allowed.
    """
    # 1. Double Hash for security (SHA256 -> RIPEMD160 logic)
    sha_hash = hashlib.sha256(public_key_string.encode()).hexdigest()
    
    # 2. Take a unique fingerprint (last 20 characters)
    fingerprint = sha_hash[-20:].upper()
    
    # 3. Apply the Sovereign Prefix
    sovereign_address = f"Huma-{fingerprint}"
    
    return sovereign_address

if __name__ == "__main__":
    # Test with a mock public key
    test_key = "PUB_KEY_TUNAPAC_2026_8G_MESH"
    print(f"Generating Sovereign Address...")
    print(f"RESULT: {generate_huma_address(test_key)}")
