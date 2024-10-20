#Gestart op 15 oktober

import time

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

class CreateSubject:
    button_number = 0

    def __init__(self, widget_container):
        self.button_number += 1
        self.timeCount = 0
        
        showsubject = TextInput(text="Subject: ", multiline=False)
        timeInput = TextInput(multiline=False)
        addTime = Button(text="Add time")
        showtime = Label(text="Time: ")

        widget_container.add_widget(showsubject)
        widget_container.add_widget(timeInput)
        widget_container.add_widget(addTime)
        widget_container.add_widget(showtime)

        # showsubject.bind

        addTime.bind(on_press=lambda instance: self.addTime_dynamic(instance, timeInput, showtime))

    def on_enter(self, instance):
        print("Enter key pressed: ", instance.text)
    
    def addTime_dynamic(self, instance, timeInput, showtime_label):
        try:
            self.timeCount += int(timeInput.text)
            showtime_label.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass


class StartWindow(Screen):
    pass

class MainWindow(Screen):
    static_time = ObjectProperty(None)
    static_showtime = ObjectProperty(None)
    widget_container = ObjectProperty(None)

    timeCount = NumericProperty(0)
    
    def create(self):
        CreateSubject(self.widget_container)

    def addTime_static(self):
        try:
            self.timeCount += int(self.time.text)
            self.showtime.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass


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