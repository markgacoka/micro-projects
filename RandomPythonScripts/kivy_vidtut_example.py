from kivy.app import App
import random

from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
from kivy.graphics.context_instructions import Color
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

kv = '''<ScatterTextWidget>:
	orientation: 'vertical'
	TextInput:
		id: my_textinput
		font_size: 150
		size_hint_y: None
		height: 200
		text: 'default'
		on_text: root.change_color()
	FloatLayout:
		Scatter:
			center: self.parent.center
			size_hint: None, None
			size: my_label.size
			canvas.after:
				Color:
					rgba: 1, 0, 0, 0.5
				Rectangle:
					size: self.size
					pos: self.pos
			Label:
				id: my_label
				text: my_textinput.text
				font_size: 150
				color: root.text_colour
				size: self.texture_size
				canvas:
					Color:
						rgba: 0, 1, 0, 0.5
					Rectangle:
						pos: self.pos
						size: self.size

	BoxLayout:
		orientation: 'horizontal'
		size_hint_y: None
		height: 150
		Label:
			id: label1
			text: my_textinput.text[:3][::1]
			font_size: 100
			color: root.text_colour
		Label:
			id: label2
			text: my_textinput.text[-3:][::-1]
			font_size: 100
			color: root.text_colour
'''
class ScatterTextWidget(BoxLayout):
	text_colour = ListProperty([1, 0, 0, 1])

	def __init__(self, **kwargs):
		super(ScatterTextWidget, self).__init__(**kwargs)

#		with self.canvas.before:
#			Color([1,0,0,1])
#			Rectangle(pos=(0, 100), size=(300, 100))
#			Ellipse(pos=(0,400), size=(300, 100))
#			Line(points=[0, 0, 500, 600, 400, 300], close=True, width=3)

	def change_color(self, *args):
		colour = [random.random() for i in range(3)] + [1]
		self.text_colour = colour

class GeneralAI(App):
	def build(self):
		Builder.load_string(kv)
		return ScatterTextWidget()

if __name__ == '__main__':
	GeneralAI().run()
