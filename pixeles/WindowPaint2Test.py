import kivy
from kivy.uix.screenmanager import Screen
from ColorLabel import ColorLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
kivy.require("1.9.1")
import json
import pymysql
import time

def byte2Per(nbyte):
	return nbyte*(1/255)

class tercera(Screen):

    def iniciarBD(self):  ##iciar y crear tablas
        Conf = None
        with open("accesoJson.json") as jsonfile:
            Conf = json.load(jsonfile)
        self.connection = pymysql.connect(
            host=Conf['HOST'], user=Conf['DBUSER'],
            password=Conf['DBPASS'], database=Conf['DBNAME'],
            charset='utf8mb4', port=Conf['PORT'])
        if self.connection:
            print("conexion realizada")

    def ObtenerLista(self):
        self.MiCursor = self.connection.cursor()
        #        MiCursor.execute("USE Ejem01;")
        intruccion = "Select MAX(id_pixeles) from pixeles;"
        self.MiCursor.execute(intruccion)
        self.cadenas = self.MiCursor.fetchone()



    def defRojo(self,obj,obj2):
        #self.sliderR
        self.R=int(self.sliderR.value)
        print("R=", self.R)
        self.selectedColor.background_color[0]=byte2Per(self.R)

    def defVerde(self,obj,obj2):
        self.G=int(self.sliderG.value)
        print("G=", self.G)
        self.selectedColor.background_color[1]=byte2Per(self.G)

    def defAzul(self,obj,obj2):
        self.B=int(self.sliderB.value)
        print("B=",self.B)
        self.selectedColor.background_color[2]=byte2Per(self.B)

    def defAlfa(self,obj,obj2):
        self.A=int(self.sliderA.value)
        print("A=", self.A)
        self.selectedColor.background_color[3]=byte2Per(self.A)

    def btnColorear(self, obj): #####################get color
        obj.background_color=[self.selectedColor.background_color[0],
                              self.selectedColor.background_color[1],
                              self.selectedColor.background_color[2],
                              self.selectedColor.background_color[3]]
        self.selectedColor.text = str(obj.key)
        cadena="UPDATE pixeles SET Red={}, Green={}, Blue={}, Alpha={} WHERE id_pixeles={};".format(byte2Per(self.R),
                                                                                                  byte2Per(self.G),
                                                                                                  byte2Per(self.B),
                                                                                                  byte2Per(self.A),
                                                                                                    obj.key)
        self.instrucciones.append(cadena)

    def botSave(self, obj):
        for i in range(0,len(self.instrucciones),1):
            self.MiCursor.execute(self.instrucciones[i])
        self.connection.commit()
        self.saveBtn.text="guardando y saliendo"
        self.connection.close()
        time.sleep(0.7)
        self.SM.current = "pantalla1"
        


    def build(self,SM=None, DC=None):
        self.instrucciones=[]
        self.iniciarBD()
        self.ObtenerLista()
        self.SM = SM
        self.DC = DC
        """"""
        self.R = self.G = self.B = 0
        self.A = 1
        numcuadrado = 3
        mainGrid = GridLayout(rows=1, cols=2)
        leftColumn = GridLayout(rows=numcuadrado, cols=numcuadrado)
        a = []
        b = []
        # b.key=0
        for i in range(0, numcuadrado, 1):
            a.append(None)
        for i in range(0, numcuadrado, 1):
            #print(i)
            b.append(a)
        contador = 0
        for i in range(0, numcuadrado, 1):
            for j in range(0, numcuadrado, 1):
                contador += 1  #########################3 este sera e key
                b[i][j] = Button(text="")
                b[i][j].background_color = [byte2Per(0), byte2Per(0), byte2Per(0), 0]
                b[i][j].background_normal = ""
                leftColumn.add_widget(b[i][j])
                b[i][j].key = contador
                if self.cadenas[0]==None:
                    cadena="INSERT INTO pixeles VALUES ({},0,0,0,0);".format(contador)
                    self.instrucciones.append(cadena)
                else:
                    self.R=self.G=self.B=0
                    cadena="UPDATE pixeles SET Red={}, Green={}, Blue={}, Alpha={} WHERE id_pixeles={};".format(0,0,0,1,contador)
                    self.instrucciones.append(cadena)
                b[i][j].bind(on_press=self.btnColorear)
        rigthColumn = GridLayout(rows=2, cols=1)
        self.uppercorner=GridLayout(rows=2)
        self.saveBtn=Button(text="Guardar")
        self.saveBtn.bind(on_press=self.botSave)
        self.selectedColor = ColorLabel(text="")
        self.selectedColor.background_color = [0, 0, 0, 0]
        self.uppercorner.add_widget(self.saveBtn)
        self.uppercorner.add_widget(self.selectedColor)
        rigthColumn.add_widget(self.uppercorner)
##############################caja################################
        sliders = GridLayout(cols=4)
        self.sliderR = Slider(min=0, max=255, step=1, orientation="vertical",value_track=True, value_track_color=[1, 0, 0, 1])
        self.sliderG = Slider(min=0, max=255, step=1, orientation="vertical",value_track=True, value_track_color=[0, 1, 0, 1])
        self.sliderB = Slider(min=0, max=255, step=1, orientation="vertical",value_track=True, value_track_color=[0, 0, 1, 1])
        self.sliderA = Slider(min=0, max=255, step=1, value=255, orientation="vertical",value_track=True, value_track_color=[1, 1, 1, 1])
        sliders.add_widget(self.sliderR)
        sliders.add_widget(self.sliderG)
        sliders.add_widget(self.sliderB)
        sliders.add_widget(self.sliderA)
        self.sliderR.bind(on_touch_move=self.defRojo)
        self.sliderG.bind(on_touch_move=self.defVerde)
        self.sliderB.bind(on_touch_move=self.defAzul)
        self.sliderA.bind(on_touch_move=self.defAlfa)
##############################################################################333
        rigthColumn.add_widget(sliders)
        mainGrid.add_widget(leftColumn)
        mainGrid.add_widget(rigthColumn)
        self.connection.commit()
        self.add_widget(mainGrid)
        print(self.instrucciones)
        return self

if __name__ == '__main__':
    pass