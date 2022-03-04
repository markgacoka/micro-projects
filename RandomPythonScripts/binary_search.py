import random

numbers = []
size = 15

def generateList():
	for i in range(size):
		b = random.randint(10, 90)
		numbers.append(b)
		numbers.sort()

def inputValidation():
	if int(user_input) in numbers:
		print ("Checking for the middle...")
	else:
		print("The number is not among the list.")
		exit()

def displayElements():
	displaySubElements(0, (size))

def displaySubElements(low, high):
	for i in range(0, int(low)):
		print("   ", sep=" ", end="")

	for i in range(int(low), (int(high))):
		print(numbers[i], sep=" ", end=" ")
	print()

low = int(0)
high = int(size)
middle = int((low + high + 1)/2)
location = int(-1)

def binarySearch(searchElement):
	global low, high, middle, location
	while (low <= high) & (location == -1):
		displaySubElements(low, high)
		for i in range(0, int(middle)):
			print("   ", sep="", end="")
		print("*")

		if int(searchElement) == numbers[int(middle)]:
			location = middle
		elif int(searchElement) < numbers[int(middle)]:
			high = middle - 1
		else:
			low = middle + 1
		middle = (low + high + 1) /2
	return location


if __name__ == '__main__':
	generateList()
	displayElements()
	user_input = input("Please enter the number you want to be searched: ")
	inputValidation()

	position = int(binarySearch(user_input))
	if position == -1:
		print("The number was not found")
	else:
		print("The number " + str(user_input) + " was found at position " + str(position + 1))
