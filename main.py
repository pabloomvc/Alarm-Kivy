import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from Dependencies import Alarma
from Dependencies import Weather
from kivy.core.audio import SoundLoader
from datetime import datetime
import time
from kivy.clock import Clock
import webbrowser as wb
from gtts import gTTS
import os
from playsound import playsound

song_name ='finale.mp3'

class MainWindow(Screen):
    hora = ObjectProperty(None)
    minuto = ObjectProperty(None)

    def btn(self):
        print("Alarma puesta a las {}:{}".format(self.hora.text,self.minuto.text))
        #Llamar a una funcion de modulo alarma a la que le paso la hora ingresada, calcula el tiempo hasta la hora ingresada, y
        #devuelve ese tiempo. Con ese tiempo, luego llamo al modulo clock para programar el sonido de la alarma
        Alarma.test()
        if self.hora.text=="" or self.minuto.text=="": #Sets the alarm at 6:30 by default if there´s no otehr input
            self.hora.text= "6"
            self.minuto.text = "30"
        t = Alarma.dt(self.hora.text,self.minuto.text) #Calculates in how long we should schedule the alarm to ring
        Clock.schedule_once(lambda dt: Ring(), t)
        self.hora.text = ""
        self.minuto.text = ""

def Ring():
    sound = SoundLoader.load(song_name)
    if sound:
        sound.play()

class SecondWindow(Screen):
    d = Weather.getWeather()
    weather = "The weather is {} today".format(d["description"])

    def open_website(self, site):
        wb.open("https://"+site+".com")
    
class LoopGrid(GridLayout):
    def __init__(self, **kwargs):
        super(LoopGrid, self).__init__(**kwargs)
        
        self.routine_list = GridLayout(size_hint=(0.5,1))
        self.todo_list = GridLayout(size_hint=(0.5,1))

        self.todo_list.cols = 1
        self.routine_list.cols = 1
        
        # ROUTINE LIST
        self.routine_list.title = Label(text="Morning Routine",font_size=30,halign="left",valign="middle", size_hint=(0.3,1), pos_hint={"x":0,"y":1})
        self.routine_list.add_widget(self.routine_list.title)
        routine = open("Texts/Routine.txt","r")
        for line in routine:
            print(line.rstrip("\n"))
            self.routine_list.item = FloatLayout(size=(1,1),pos_hint={"x":0})
            
            self.routine_list.item.cols = 2
            self.itm_chk = CheckBox(active=False, size_hint=(0.1,1), pos_hint={"x":0.2, "y":0})
            self.itm_chk.bind(active = self.on_checkbox_Active)
            self.itm_lbl = Label(text=line.rstrip('\n'),text_size = self.size, halign="left",valign="middle", size_hint=(0.3,1), pos_hint={"x":0.35, "y":0})
            
            self.routine_list.item.add_widget(self.itm_chk)
            self.routine_list.item.add_widget(self.itm_lbl)
            self.routine_list.add_widget(self.routine_list.item)
        routine.close()
        self.add_widget(self.routine_list)

        # TO_DO_LIST
        self.todo_list.title = Label(text="To Do",font_size=30,halign="left",valign="middle", size_hint=(0.3,1), pos_hint={"x":0,"y":1})
        self.todo_list.add_widget(self.todo_list.title)
        todo = open("Texts/TODO.txt","r")
        for line in todo:
            item = Label(text=line.rstrip('\n'))
            self.todo_list.add_widget(item)
        todo.close()
        self.add_widget(self.todo_list)
        

    # Callback for the checkbox 
    def on_checkbox_Active(self, checkboxInstance, isActive): 
        if isActive: 
            #self.itm_lbl.text ="Checkbox is ON"
            print("Checkbox Checked") 
        else: 
            print("Checkbox unchecked") 



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    MyApp().run()