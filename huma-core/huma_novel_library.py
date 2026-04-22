class HumaNovel:
    def __init__(self):
        self.authors = ["Wole Soyinka", "Chinua Achebe", "Ola Rotimi", "Shakespeare"]
        self.history = ["Hausa/Fulani Emirate", "Yoruba Alaafin", "Igbo Segmentary"]

    def get_lesson(self, category):
        if category == "Nationalists":
            return "Herbert Macaulay: The Father of Nigerian Nationalism and the NNDP (1923)."
        if category == "Literature":
            return "Macbeth: The ambition trap. Shylock: The debt-justice paradox."
        return "Accessing Huma Global Education Database..."

if __name__ == "__main__":
    lib = HumaNovel()
    print(f"\n[HUMANOVEL]: {lib.get_lesson('Nationalists')}")
