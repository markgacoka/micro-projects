def beginProgram():
	print()
	print("Factorials use a recursive function to get the multiplication of all the numbers down the number line e.g. 3! = 3 x 2 x 1")
	print()
	print("Do you want to ?")
	print("1: Get the factorial of a number.")
	print("2: Get the sequence of factorials upto a number of your choice.")

def chooseOption():
	if (choice != 1 and choice != 2):
		print("Wrong choice.")
	elif choice == 1:
		number = int(input("Which number do want to know the factorial of: "))
		print("The factorial of " + str(number) + " also represented as " + str(number) + "! is " + str(getFactorial(number)))
	else:
		number = int(input("Enter the number of sequences to get the factorial of: "))
		getSequence(number)


def getFactorial(number):
	if number < 0:
		print("The number should not be negative.")
	elif number == 0 or number == 1:
		return 1
	else:
		return number * getFactorial( number - 1)

def getSequence(number):
	print("The first " + str(number) + " number(s) of the sequence are: ")
	sequence = []
	for i in range(number):
		sequence.append(getFactorial(i))
	print(*sequence, sep=", ")

if __name__ == '__main__':
	beginProgram()
	choice = int(input("Choose 1 or 2: "))
	chooseOption()
