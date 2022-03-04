import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatingApp(App):
	def build(self):
		return FloatLayout() #button size and background color did not apply. Objective: anchoring buttons to window edges.

if __name__ == '__main__':
	FloatingApp().run()