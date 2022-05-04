# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:23:27 2022

@author: ghost
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from ColorLabel import ColorLabel
import random

def byte2Per(nbyte):
	return nbyte*(1/255)


class sqlapp(App):
    def btnaccion_press(self,obj):
        gen = random.Random()
        Dado1 = 0
        Dado1 = gen.randint(1,6)
        self.lblnumdado.text = str(Dado1)
		
	# Este es el constructor
    def __init__(self,**kwargs):
		# llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
		#Defino un atributo
		
    def build(self):
		# Vamos a definir un layout
        gdl_principal = GridLayout(cols=3)
		############################################
        lbltitulo = self.label = ColorLabel(text='hola')
        self.label.background_color = [byte2Per(255),byte2Per(150),byte2Per(170),1]
		############################################
        gdl_principal.add_widget(lbltitulo)
        
        #Grid medio
        gdl_medio = GridLayout(rows=5)
        lblresultado = self.label = ColorLabel(text='Resultado:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado)
        lblresultado1 = self.label = ColorLabel(text='Resultado1:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado1)
        lblresultado2 = self.label = ColorLabel(text='Resultado2:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado2)
        lblresultado3 = self.label = ColorLabel(text='Resultado3:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado3)
        lblresultado4 = self.label = ColorLabel(text='Resultado4:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado4)


        prueba = gdl_medio
        self.label.background_color = [byte2Per(220),byte2Per(100),byte2Per(170),1]
		############################################
        gdl_principal.add_widget(prueba)
        """
		#Grid medio
        gdl_medio = GridLayout(rows=5)
        lblresultado = self.label = ColorLabel(text='Resultado:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado)
        lblnumdado = self.label = ColorLabel(text='hgfhg')
        self.label.background_color = [1,0,1,1]
        gdl_medio.add_widget(lblnumdado)
        gdl_principal.add_widget(gdl_medio)
        
        lblresultado1 = self.label = ColorLabel(text='Resultado:')
        self.label.background_color = [0.9,0,0.80,1]
        gdl_medio.add_widget(lblresultado1)
        lblnumdado1 = self.label = ColorLabel(text='hgfhg')
        self.label.background_color = [1,0,1,1]
        gdl_medio.add_widget(lblnumdado1)
        lblnumdado2 = self.label = ColorLabel(text='hgfhg')
        self.label.background_color = [1,0,1,1]
        gdl_medio.add_widget(lblnumdado2)
        gdl_principal.add_widget(gdl_medio)
        """
        
		#Boton
        btnaccion = Button(text="Presionanme!!!")
        gdl_principal.add_widget(btnaccion)
        btnaccion.bind(on_press = self.btnaccion_press)
       # btnaccion.bind(on_press=self.btn_press)
        self.gdl_principal = gdl_principal
        #self.lblnumdado = lblnumdado
        return gdl_principal

if __name__ == '__main__':
	D = sqlapp()
	D.run()
