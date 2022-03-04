import kivy
from kivy.app import App
from kivy.uix.stacklayout import StackLayout

class StackLayoutApp(App):
	def build(self):
		return StackLayout() #arranges widgets horizontally or vertically as they best fit on screen

if __name__ == '__main__':
	StackLayoutApp().run()