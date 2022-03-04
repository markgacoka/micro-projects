import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class BoxLayoutApp(App):
	def build(self):
		return BoxLayout() #first button takes 70% of allocated width and 50% of what it would have been allocated if equal

if __name__ == '__main__':
	BoxLayoutApp().run()