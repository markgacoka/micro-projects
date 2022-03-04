from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')

class ClearText(App, BoxLayout):
	def build(self):
		self.box = BoxLayout(orientation='horizontal', spacing=20)
		self.txt = TextInput(hint_text="Write here", size_hint=(.5,.1))
		self.buttn = Button(text="Clear All", on_press=self.clear, size_hint=(.1,.1))

		self.box.add_widget(self.txt)
		self.box.add_widget(self.buttn)
		return self.box

	def clear(self, instance):
		self.txt.text = ''

if __name__=='__main__':
	ClearText().run()
