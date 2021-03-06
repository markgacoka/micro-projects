#radios, check boxes, switches and sliders

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup


class CustomPopup(Popup):
	pass

class SampBoxLayout(BoxLayout):
	checkbox_is_active = ObjectProperty(False)

	def checkbox_clicked(self, instance, value):
		if value is True:
			print("Checkbox is checked")
		else:
			print("Checkbox is unchecked")

	#radio buttons
	blue = ObjectProperty(True)
	red = ObjectProperty(False)
	green = ObjectProperty(False)

	def switch_on(self, instance, value):
		if value is True:
			print("Switch on")
		else:
			print("Switch off")

	def open_popup(self):
		the_popup = CustomPopup()
		the_popup.open()

	def spinner_clicked(self, value):
		print("Spinner Value: " + value)

class SampleApp(App):
	def build(self):
		Window.clearcolor = (1, 1, 1, 1)
		return SampBoxLayout()

if __name__ == '__main__':
	SampleApp().run()