#Gestart op 15 oktober 2024

import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class StartWindow(Screen):
    pass

class MainWindow(Screen):
    timeCount = NumericProperty(0)

    time = ObjectProperty(None)
    showtime = ObjectProperty(None)
    widget_container = ObjectProperty(None)

    def addTime(self):
        try:
            self.timeCount += int(self.time.text)
            self.showtime.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass
    
    def create(self):
        new_subject = Label(text="New Subject")
        new_subject_timeInput = TextInput(text="test", multiline=False)
        new_subject_addTime = Button(text="Add time")
        new_subject_showtime = Label(text="Time: ")

        self.widget_container.add_widget(new_subject)
        self.widget_container.add_widget(new_subject_timeInput)


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("timespenton.kv")

class TimeSpentOn(App):
    def build(self):
        #Window.maximize()

        self.title = "Time Spent On"
        return kv
    
if __name__ == "__main__":
    TimeSpentOn().run()