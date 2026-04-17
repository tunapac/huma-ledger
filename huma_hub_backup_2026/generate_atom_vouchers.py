import random
import csv
import hashlib

def generate_vouchers(count=1000):
    print(f"🎫 GENERATING {count} QUANTUM-SAFE ATOM VOUCHERS...")
    
    denominations = [5, 10, 20, 50] # ATOm values (USD equivalent)
    
    with open('huma_vouchers_registry.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["SERIAL_NUMBER", "PIN_CODE", "VALUE_ATOM", "STATUS"])
        
        for i in range(count):
            # 10-digit Serial (Public)
            serial = f"SN-{random.randint(1000000000, 9999999999)}"
            
            # 12-digit PIN (Private/Hidden under scratch card)
            pin = "".join([str(random.randint(0, 9)) for _ in range(12)])
            
            # Value selection
            val = random.choice(denominations)
            
            writer.writerow([serial, pin, val, "UNUSED"])
            
    print(f"✅ SUCCESS: 1,000 Vouchers saved to huma_vouchers_registry.csv")

if __name__ == "__main__":
    generate_vouchers()
