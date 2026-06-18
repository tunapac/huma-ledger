import segno
import time
import hashlib
import json
import os

# Your root key for the 5B Node Mesh
SECRET_SALT = "HUMA_SOVEREIGN_KEY_5B"

def generate_dynamic_token(asset_id):
    timestamp = str(int(time.time()))
    raw_data = f"{asset_id}:{timestamp}"
    token = hashlib.sha256((raw_data + SECRET_SALT).encode()).hexdigest()
    return f"huma://verify/{asset_id}/{token}"

def run_bulk_generation(asset_list_file):
    output_dir = "huma_qr_inventory"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(asset_list_file, 'r') as f:
        assets = json.load(f)
        
    for asset in assets:
        asset_id = asset['id']
        asset_name = asset['name']
        
        payload = generate_dynamic_token(asset_id)
        qr = segno.make_qr(payload)
        
        # Save filename corresponding to Asset ID
        filename = f"{output_dir}/huma_qr_{asset_id}.png"
        qr.save(filename, scale=10)
        print(f"Generated secure QR for: {asset_name} ({asset_id})")

if __name__ == "__main__":
    # Create a sample asset list for demonstration
    sample_assets = [
        {"id": "NODE_ALPHA_001", "name": "5B-Mesh Gateway Node"},
        {"id": "PROD_TUNA_PACK_v2", "name": "Authenticated Tunapac Container"},
        {"id": "HSN_CORE_SERVER", "name": "Registry Management Unit"}
    ]
    with open('asset_inventory.json', 'w') as f:
        json.dump(sample_assets, f)
        
    print("--- Starting Bulk HSN QR Generation ---")
    run_bulk_generation('asset_inventory.json')
    print(f"✅ Bulk generation complete. Check the 'huma_qr_inventory' folder.")
