from huma_linguistics import HumaLinguistics

class GlobalTerminal:
    def __init__(self, location):
        self.translator = HumaLinguistics()
        self.location = location

    def display_welcome(self, target_lang):
        msg = "Welcome to Tunapac Humanledger. Insert huma_ ID."
        translated = self.translator.universal_translate(msg, target_lang)
        print(f"\n[TERMINAL-{self.location}]: {translated}")

if __name__ == "__main__":
    terminal = GlobalTerminal("Lagos-Hub")
    terminal.display_welcome("igbo")
