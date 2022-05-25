import kivy
from kivy.uix.screenmanager import Screen
kivy.require('1.9.0')
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import json
import pymysql
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class primera(Screen):

    def iniciarBD(self):  ##iciar y crear tablas
        instrucciones = []
        cadena = """create table if not exists pixeles(id_pixeles smallint(5)  unsigned primary KEY auto_increment,
                    Red float(3,2) unsigned,
                    Green float(3,2) unsigned,
                    Blue float(3,2) unsigned,
                    Alpha float(3,2) unsigned)engine=InnoDB;"""
        instrucciones.append(cadena)
        Conf = None
        with open("accesoJson.json") as jsonfile:
            Conf = json.load(jsonfile)
        self.connection = pymysql.connect(
            host=Conf['HOST'], user=Conf['DBUSER'],
            password=Conf['DBPASS'], database=Conf['DBNAME'],
            charset='utf8mb4', port=Conf['PORT'])
        if self.connection:
            print("conexion realizada")
            self.MiCursor = self.connection.cursor()
            #        MiCursor.execute("USE Ejem01;")
            for i in range(0, len(instrucciones), 1):
                print(instrucciones[i])
                self.MiCursor.execute(instrucciones[i])
            self.connection.commit()
            self.connection.close()

            # result=MiCursor.fetchall()
            # for i in range(0,len(result),1):
            # print(result[i]

    def btnIniciar(self, obj):
        self.SM.current = "pantalla2"


    def btnReporte(self, obj):
        Conf = None
        with open("accesoJson.json") as jsonfile:
            Conf = json.load(jsonfile)
        connectionReporte = pymysql.connect(
            host=Conf['HOST'], user=Conf['DBUSER'],
            password=Conf['DBPASS'], database=Conf['DBNAME'],
            charset='utf8mb4', port=Conf['PORT'])
        if connectionReporte:
            print("conexion realizada")
            MiCursor = connectionReporte.cursor()
        c = canvas.Canvas("DIBUJO.pdf", pagesize=letter)
        instruccion="Select MAX(id_pixeles) from pixeles;"
        MiCursor.execute(instruccion)
        cadenas = MiCursor.fetchone()
        if cadenas[0]==None:
            c.line(40, 660, 572, 660)
            c.drawCentredString(306, 661, "NO SE HAN ENCONTRADO RESULTADOS")
            c.showPage()
        else:
            instruccion = "Select * from pixeles;"
            MiCursor.execute(instruccion)
            cadenas = MiCursor.fetchall()
            print("len de cadenas: ", len(cadenas))
            for i in range(0,len(cadenas),1):
                print(cadenas[i][0])
                print(cadenas[i][1])
                print(cadenas[i][2])
                print(cadenas[i][3])
                print(cadenas[i][4])
            c.line(40, 720, 572, 720)
            c.drawCentredString(93, 705, "id_pixel")
            c.drawCentredString(199.25, 705, "Red")
            c.drawCentredString(305.75, 705, "Green")
            c.drawCentredString(412.25, 705, "Blue")
            c.drawCentredString(518.5, 705, "Alpha")
            c.line(40, 700, 572, 700)
            a = 700
            for i in range(0, len(cadenas), 1):
                b = a
                a = a - 20
                c.line(40, a, 572, a) #linea inferior
                c.line(40, b, 40, a)#primer linea vertical
                c.drawCentredString(93, a+5, str(cadenas[i][0]))
                c.line(146, b, 146, a)#
                c.drawCentredString(199.25, a+5, str(cadenas[i][1]))
                c.line(252.5, b, 252.5, a)
                c.drawCentredString(305.75, a+5, str(cadenas[i][2]))
                c.line(359, b, 359, a)
                c.drawCentredString(412.25, a+5, str(cadenas[i][3]))
                c.line(465.5, b, 465.5, a)
                c.drawCentredString(518.5, a+5, str(cadenas[i][4]))
                c.line(572, b, 572, a)
        c.save()

    def build(self, SM=None, DC=None):
        ##iniciarBD()
        ###########esta variable tiene una referencia al screen manager
        self.SM=SM
        self.DC=DC
        self.iniciarBD()
        mainGrid=GridLayout(rows=3)
        upperGrid=GridLayout(cols=2)
        upperGrid.add_widget(Image(source='firma 2022.png'))
        upperGrid.add_widget(Image(source='5d7bb8ca55a60350e3fde9de167e7e25.jpg'))
        mainGrid.add_widget(upperGrid)
        botonIniciar=Button(text="iniciar")
        botonIniciar.bind(on_press=self.btnIniciar)
        botonReporte = Button(text="GenerarReporte")
        botonReporte.bind(on_press=self.btnReporte)
        mainGrid.add_widget(botonIniciar)
        mainGrid.add_widget(botonReporte)
        self.add_widget(mainGrid)
        return self

if __name__ == '__main__':
    """window=primaria()
    window.iniciarBD()
    window.run()"""
    pass