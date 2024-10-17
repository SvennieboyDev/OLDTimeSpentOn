#Gestart op 15 oktober 2024

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.title = "Time Spent On"
        layout = GridLayout(cols=2)
        layout.add_widget(Label(text="Time Spent On"))
        layout.add_widget(Label(text="15 October 2024"))
        return layout
    
if __name__ == "__main__":
    MyApp().run()