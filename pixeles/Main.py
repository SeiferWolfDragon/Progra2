import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
####################aqui se importan las pantallas
from primaryWindow import primera
#from secondWindow import segunda
from WindowPaint2Test import tercera
from DatosCompartidos import DatosCompartidos
class Principal(App):
    def build(self):
        mPantalla=ScreenManager()
        #########dos sintaxis
        #
        DcCompa=DatosCompartidos()
        p1=primera(name="pantalla1")
        p1.build(SM=mPantalla, DC=DcCompa)

        #p2=segunda(name="pantalla2").build(SM=mPantalla, DC=DcCompa)
        p2=tercera(name="pantalla2").build(SM=mPantalla, DC=DcCompa)
        mPantalla.add_widget(p1)
        #mPantalla.add_widget(p2)
        mPantalla.add_widget(p2)
        mPantalla.current="pantalla1"
        return mPantalla

if __name__=='__main__':
    miapp=Principal()
    miapp.run()