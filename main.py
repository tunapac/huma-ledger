from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HumanityLedgerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        label = Label(text='Humanity Ledger\nStatus: Active\nSupply: 700,000,000 HUMA', 
                      halign='center', font_size='20sp')
        layout.add_widget(label)
        return layout

if __name__ == '__main__':
    HumanityLedgerApp().run() 
