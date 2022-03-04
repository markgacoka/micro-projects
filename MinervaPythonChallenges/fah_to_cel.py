#Q2. Convert Farenheit degrees to Celsius using formula
def fah_to_cel_converter(degrees):
	#define the equation and equate it to an integer variable 'celsius' then print out the result
	celsius = 5/9*(degrees - 32)
	celsius = round(celsius, 2)
	print(celsius)

if __name__=='__main__':
	fah_to_cel_converter(3)
	fah_to_cel_converter(90)
