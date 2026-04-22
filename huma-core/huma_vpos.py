from huma_linguistics import HumaLinguistics

class HumaVirtualPOS:
    def __init__(self, merchant_huma_id):
        self.merchant_id = merchant_huma_id
        self.tax_rate = 0.00888
        self.translator = HumaLinguistics()

    def generate_payment_qr(self, amount, currency, target_lang="english"):
        tax = amount * self.tax_rate
        total = amount + tax
        
        msg = f"Pay {total:.2f} {currency} (Tax: {tax:.2f})"
        translated_msg = self.translator.universal_translate(msg, target_lang)
        
        print(f"\n[V-POS]: {translated_msg}")
        print(f"[STATUS]: Routing 0.888% to Treasury: huma_G888SovereignAdmin")
        return "QR_CODE_DATA_GENERATED"

if __name__ == "__main__":
    vpos = HumaVirtualPOS("huma_MerchantAlpha1")
    vpos.generate_payment_qr(5000, "NGN", "yoruba")
