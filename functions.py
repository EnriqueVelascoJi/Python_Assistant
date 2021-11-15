# -*- coding: utf-8 -*-
"""

@author: Enrique Velasco Jimenez
         Emiliano Morales Camacho 
"""
import webbrowser
from db import *

#Function that change from a boy to a girl
def change_to_girl(list_words):
    
    if 'girl' in list_words:
        return True

#Algorithm to select the correct answer
def proccess_to_select(words):
    global_counter = []
    counter = 0
    
    for value in answers.values():
        list_to_evaluate = value
        for word in words:
            if word in list_to_evaluate:
                counter += 1
        global_counter.append(counter)
        counter = 0
    
    max_value = None
    max_idx = None
    
    for idx, num in enumerate(global_counter):
        if max_value is None or num > max_value:
            max_value = num
            max_idx = idx
    
    
    return max_value, max_idx

#Select the best answer
def select_best_answer(words):
    
    number, index = proccess_to_select(words)
    
    options = list(answers.keys())
    answer_selected = options[index]
    
    if index == 33:
        webbrowser.open('https://coinmarketcap.com/')
    
    return answer_selected

    
    



