from kivy.app import App
from functools import partial
from kivy.uix.button import Button

class ButtonApp(App):
	def disable(self, instance, *args):
		instance.disabled = True

	def updateButton(self, instance, *args):
		instance.text = "I am disabled!"

	def build(self):
		my_buttn = Button(text="Click me to disable")
		my_buttn.bind(on_press=partial(self.disable, my_buttn))
		my_buttn.bind(on_press=partial(self.updateButton, my_buttn))
		return my_buttn

if __name__== '__main__':
	ButtonApp().run()
