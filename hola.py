# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:34:11 2022

@author: diego
"""

import kivy
import kivy.app
import kivy.uix.label

class FirstApp(kivy.app.App):
    
    def built(self):
        return kivy.uix.label.Label(text = "hi world")
    
FirstApp().run()