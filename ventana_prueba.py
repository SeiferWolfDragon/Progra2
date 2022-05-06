# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:23:27 2022

@author: Giovanni Jair Sanchez Chimal
        Juan Diego Vazquez Hernandez
"""
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from ColorLabel import ColorLabel
<<<<<<< HEAD
import json
import pymysql.cursors

=======
from kivy.uix.textinput import TextInput
import json
import pymysql.cursors
>>>>>>> 3563363813ea4acb1c18c4ccacd5bd8fdfd2ab45

def byte2Per(nbyte):
	return nbyte*(1/255)


<<<<<<< HEAD
class sqlapp(App):

    """def btnok_press(self, obj):
        if self.connecction:
            print(self.txtusr.text, self.txtpwd.text)
            nick = self.txtusr.text
            passwd = self.txtpwd.text
            MiCursor = self.connection.cursor()
            # SQL A EJECUTAR
            SQL = "SELECT * FROM usuario where nick = %s and sword = sha256(%s,256)"
            MiCursor.execute(SQL, [nick, passwd])
            Resultado = MiCursor.fetchone()
            if Resultado:
                self.col2.text = "Acceso concedido"
                print("Acceso concedido")
            else:
                self.col2.text = "Acceso no concedido"
                print("Acceso no concedido")
        else:
            print("nah")

    def iniciarDB(self):
        self.Conf = None
        with open("db.json") as jsonfile:
            self.Conf = json.load(jsonfile)
        self.connection = pymysql.connect(host=self.Conf["HOST"],
                                          user=self.Conf["DBUSER"],
                                          password=self.Conf["DBPASS"],
                                          database=self.Conf["DBNAME"],
                                          charset='utf8mb4',
                                          port=self.Conf["PORT"])"""
		
	# Este es el constructor
    def __init__(self,**kwargs):
		# llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
		#Defino un atributo
		
    def build(self):
		# Vamos a definir un layout
        #layout principal
        gdl_principal = GridLayout(cols=3)
        lbl_izq = self.label = ColorLabel(text='hola')
        self.label.background_color = [byte2Per(128),byte2Per(179),byte2Per(255),1]
        gdl_principal.add_widget(lbl_izq)
        
        #Grid medio
        self.col_medio = GridLayout(rows=5)
        self.row_usr = self.label = ColorLabel(text='Usuario:')
        self.label.background_color = [byte2Per(255),byte2Per(0),byte2Per(0),1]
        self.col_medio.add_widget(self.row_usr)
        self.usr_txt = TextInput(text='')
        self.col_medio.add_widget(self.usr_txt)
        self.row_pwd = self.label = ColorLabel(text='Contraseña')
        self.label.background_color = [byte2Per(255),byte2Per(0),byte2Per(0),1]
        self.col_medio.add_widget(self.row_pwd)
        self.pwd_txt = TextInput(text='')
        self.col_medio.add_widget(self.pwd_txt)
        self.btn_login = Button(text="Continuar")
        self.label.background_scolor = [byte2Per(255), byte2Per(0), byte2Per(0), 1]
        #self.btn_login =
        self.col_medio.add_widget(self.btn_login)



        prueba = self.col_medio
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
       # btnaccion.bind(on_press = self.btnaccion_press)
       # btnaccion.bind(on_press=self.btn_press)
        self.gdl_principal = gdl_principal
        #self.lblnumdado = lblnumdado
        return gdl_principal
=======
class Acceso(App):
    def botonok_press(self,obj):
        if self.connection:
            nick = self.inputUsuario.text
            password = self.inputUsuario.text
            Mi_cursor = self.connection.cursor()
            #SQL a ejecutar
            SQL = 'Select * from usuario where nick = %s and password = sha2(%s,256)'
            #Print Sql
            Mi_cursor.execute(SQL,[nick,password])
            Resultado = Mi_cursor.fetchone()
            if Resultado:
                self.columna2.text = 'Acceso Concedido'
                print('Acceso Concedido')
            else:self.columna2.text = 'Acceso no concedido'
            print('Acceso no concedido')
        else:
            print('Error')
    def iniciarBD(self):
        self.conf= None
        with open('db.json') as jsonfile:
            self.conf = json.load(jsonfile)
            
        self.connection = pymysql.connect(
            host=self.conf['HOST'], user=self.conf['DBUSR'],
            password=self.conf['DBPASS'], database=self.conf['DBNAME'],
            charset='utf8mb4', port=self.conf['PORT']
            )
        
    def build(self):
		# Vamos a definir un layout
        self.gdl_principal = GridLayout(cols=3)
        self.gdl_medio = GridLayout(rows =5)
		############################################
        self.labelusuario = ColorLabel(text='Usuario')
        self.labelusuario.background_color=[1,0,0,1]
        self.inputUsuario = TextInput(text='')
        self.labelpassword = ColorLabel(text='Contraseña')
        self.labelpassword.background_color=[1,0,0,1]
        self.inputpassword = TextInput(text='')
        self.botonok = Button(text='Accesar')
        self.botonok.background_color=[0,0,0,1]
        
		############################################
        self.gdl_medio.add_widget(self.labelusuario)
        self.gdl_medio.add_widget(self.inputUsuario)
        self.gdl_medio.add_widget(self.labelpassword)
        self.gdl_medio.add_widget(self.inputpassword)
        self.gdl_medio.add_widget(self.botonok)
        #############################################
        self.botonok.bind(on_press=self.botonok_press)
        ###############################################33
        columna1=ColorLabel(text='')
        columna1.background_color=[0.5,0.7,1,1]
        self.columna2=ColorLabel(text='')
        self.columna2.background_color=[0.5,0.7,1,1]
        self.gdl_principal.add_widget(columna1)
        self.gdl_principal.add_widget(self.gdl_medio)
        self.gdl_principal.add_widget(self.columna2)
        return self.gdl_principal
        
>>>>>>> 3563363813ea4acb1c18c4ccacd5bd8fdfd2ab45

if __name__ == '__main__':
    SQLApp = Acceso()
    SQLApp.iniciarBD()
    SQLApp.run()
    #Esto ejecuta el entrono grafico
    
