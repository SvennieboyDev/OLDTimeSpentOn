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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class CreateSubject:
    button_number = 0

    def __init__(self, widget_container):
        self.button_number += 1
        self.timeCount = 0
        
        give_name_layout = BoxLayout(orientation="vertical")
        self.changeSubjectInput = TextInput(text="New subject", multiline=False)
        change_subject = Button(text="Confirm")
        give_name_layout.add_widget(self.changeSubjectInput)
        give_name_layout.add_widget(change_subject)

        timeInput = TextInput(multiline=False)
        addTime = Button(text="Add time")
        showtime = Label(text="Time: ")

        widget_container.add_widget(give_name_layout)
        widget_container.add_widget(timeInput)
        widget_container.add_widget(addTime)
        widget_container.add_widget(showtime)

        addTime.bind(on_press=lambda instance: self.addTime_dynamic(instance, timeInput, showtime))
        change_subject.bind(on_press=lambda instance: self.change_subject_name(instance, change_subject, give_name_layout))
    
    def addTime_dynamic(self, instance, timeInput, showtime_label):
        try:
            self.timeCount += int(timeInput.text)
            showtime_label.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass
    
    def change_subject_name(self, instance, changeSubjectBtn, ChangeSubjectLayout):
        try:
            if changeSubjectBtn.text == "Confirm":
                changeSubjectBtn.text = "Change"

                self.new_subject_name = self.changeSubjectInput.text
                ChangeSubjectLayout.remove_widget(self.changeSubjectInput)

                self.subject_name = Label(text=self.new_subject_name)
                ChangeSubjectLayout.add_widget(self.subject_name, index=1)
            else:
                changeSubjectBtn.text = "Confirm"

                ChangeSubjectLayout.remove_widget(self.subject_name)

                self.changeSubjectInput = TextInput(text=self.new_subject_name, multiline=False)
                ChangeSubjectLayout.add_widget(self.changeSubjectInput, index=1)
        except ValueError:
            pass


class StartWindow(Screen):
    pass

class MainWindow(Screen):
    static_time = ObjectProperty(None)
    static_showtime = ObjectProperty(None)
    widget_container = ObjectProperty(None)
    changeSubjectInput = ObjectProperty(None)
    changeSubjectBtn = ObjectProperty(None)
    changeSubjectLayout = ObjectProperty(None)

    timeCount = NumericProperty(0)
    
    def create(self):
        CreateSubject(self.widget_container)

    def addTime_static(self):
        try:
            self.timeCount += int(self.time.text)
            self.showtime.text = "Time: " + str(self.timeCount)
        except ValueError:
            pass
    
    def change_subject_name(self):
        try:
            if self.changeSubjectBtn.text == "Confirm":
                self.changeSubjectBtn.text = "Change"

                self.new_subject_name = self.changeSubjectInput.text
                self.changeSubjectLayout.remove_widget(self.changeSubjectInput)

                self.subject_name = Label(text=self.new_subject_name)
                self.changeSubjectLayout.add_widget(self.subject_name, index=1)
            else:
                self.changeSubjectBtn.text = "Confirm"

                self.changeSubjectLayout.remove_widget(self.subject_name)

                self.changeSubjectInput = TextInput(text=self.new_subject_name, multiline=False)
                self.changeSubjectLayout.add_widget(self.changeSubjectInput, index=1)
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