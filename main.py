#Gestart op 15 oktober 2024

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

class StartWindow(Screen):
    pass

class MainWindow(Screen):
    time = ObjectProperty(None)
    showtime = ObjectProperty(None)
    widget_container = ObjectProperty(None)

    timeCount = NumericProperty(0)
    button_number = 0
    new_timeCounts = {}
    
    def create(self):
        self.button_number += 1
        self.new_timeCounts[self.button_number] = 0

        #new_subject = Label(text="New Subject")
        new_subject_timeInput = TextInput(multiline=False)
        new_subject_addTime = Button(text="Add time")
        new_subject_showtime = Label(text="Time: ")

        self.widget_container.add_widget(new_subject_timeInput)
        self.widget_container.add_widget(new_subject_addTime)
        self.widget_container.add_widget(new_subject_showtime)

        new_subject_addTime.bind(on_press=lambda instance: self.addTime_dynamic(instance, new_subject_timeInput, new_subject_showtime, self.button_number, self.new_timeCounts))

    def addTime_static(self):
        try:
            self.timeCount += int(self.time.text)
            self.showtime.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass
    
    def addTimeBtnPress():
        pass
    
    def addTime_dynamic(self, instance, textInput, showtime_label, button_number, timeCounts):
        try:
            new_timeCount = timeCounts[button_number]
            new_timeCount += int(textInput.text)
            timeCounts[button_number] = new_timeCount
            showtime_label.text = "Time: " + str(new_timeCount)
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