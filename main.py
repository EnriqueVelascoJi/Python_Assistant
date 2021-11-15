# -*- coding: utf-8 -*-
"""
@author: Enrique Velasco Jimenez
         Emiliano Morales Camacho   
"""

import pyttsx3
import speech_recognition as sr
from functions import *

class Assiatant:
    
    engine = pyttsx3.init() #Init the speaker
    voices = engine.getProperty('voices') #Get voices of the speaker
    
    def __init__(self):
        
        self.engine.setProperty('rate', 125)
        self.engine.setProperty('voice', self.voices[2].id) #We start with a boy voice
    
    #The assistan speak
    def speak(self, speech):
        self.engine.say(speech)
        self.engine.runAndWait()
    
    #The assistan listen
    def listen(self):
        r = sr.Recognizer() 
        
        try: 
            with sr.Microphone() as source:
                print("Tell something")
                audio = r.listen(source)
                text_recognized = r.recognize_google(audio, language="en-US")
                print(text_recognized)
                return text_recognized
        except:
            self.speak("I can not understand")
            return "ERROR"
    
    #The assistan select the answer
    def select_answer(self, text_recognized, fil):
        
        text_recognized_list = text_recognized.split(" ")
        
        if fil == 0:
            return change_to_girl(text_recognized)
        else:
            return select_best_answer(text_recognized_list)
    
    #Change the voice of a speaker
    def change_speaker(self):
        self.engine.setProperty('voice', self.voices[1].id) #We change to a girl voice
        
    #Good Bye for the assistant
    def good_bye(self):
        self.speak("Good Bye, have a nice day")
    
    #Presentation of the assistant
    def presentation(self):
        
        self.speak("Hi!, Would yo like to take the conversation with a boy or girl")
        option_recognized = self.listen()
        answer = self.select_answer(option_recognized, 0)
        if answer:
            self.change_speaker()
        
        self.speak('''Welcome to Crypto assistant, how can I help you''')
    
    #Start the process
    def start(self):
        #Presentation
        self.presentation()
        
        while True:
            question_recognized = self.listen()
            answer = self.select_answer(question_recognized, 1)
            
            if answer != "finished":
                self.speak(answer)
            else:
                break
            
        
        #GoodBye
        self.good_bye()
        

crypto_assistant = Assiatant()
crypto_assistant.start()

