from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from ColorLabel import ColorLabel
class MyApp(App):
	def btn_press(self,Obj):
		self.label.background_color = [0,1,0,1]
	def btn1_press(self,Obj):
		self.label.background_color = [1,0,0,1]
		
	def build(self):
		layout = GridLayout(rows=3)
		self.label = ColorLabel(text='test')
		self.label.background_color = [0.75,0,0,1]
		btn = Button(text="cambiar")
		btn1 = Button(text="cambiar2")
		layout.add_widget(btn)
		layout.add_widget(btn1)
		layout.add_widget(self.label)
		btn.bind(on_press=self.btn_press)
		btn1.bind(on_press=self.btn1_press)
		return layout


if __name__ == '__main__':
	MyApp().run()
