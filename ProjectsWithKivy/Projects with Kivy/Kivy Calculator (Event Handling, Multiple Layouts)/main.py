import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGrid(GridLayout):
	def calculate(self, calculation):
		if calculation:
			try:
				self.display.text = str(eval(calculation))
			except Exception:
				self.display.text = "Error"

class CalculatorApp(App):
	title = "Calculator App"
	def build(self):
		return CalcGrid()

if __name__ == '__main__':
	CalculatorApp().run()