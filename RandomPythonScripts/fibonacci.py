import time
import math
import functools

def beginProgram():
	print()
	text = "************************WELCOME************************"
	for i in range(len(text)):
		print(*text[i], sep="", end="", flush=True)
		time.sleep(0.05)

	print()
	text_two = "You will be guided through the Fibonacci Knowledgebase."
	epoch = 1
	for j in range(len(text_two)):
		print(*text_two[j], sep="", end="", flush=True)
		time.sleep(0.1)
		epoch = epoch / 2

	print("\n")
	print("Press 1 to display the Fibonacci Series (upto a certain number)")
	time.sleep(1)
	print("Press 2 to display the value of a number in the sequence")
	time.sleep(1)
	print("Press 3 to check if a number is a Fibonacci number.")
	time.sleep(1)

@functools.lru_cache(None)
def fibonacci(a):
	if a == 0 or a == 1:
		return a
	else:
		return (fibonacci(a - 1) + fibonacci(a - 2))


def displayFibonacciSeries(n):
	if n<= 0:
		print("Please enter a number greater than zero.")
	else:
		fibonacciSequence = []
		for n in range(n):
			fibonacciSequence.append(fibonacci(n))
		print(*fibonacciSequence, sep=", ", end=".")
		print()

def checkFibonacciNumber(n):
	y = 0
	def isPerfectSquare(x):
		r = int(math.sqrt(x))
		return r * r == x

	def isFibonacci(n):
		return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
	if isFibonacci(n) == True:
		while fibonacci(y) != n:
			y += 1
		if y%10 == 1:
			print("The number " + str(n) + " is a Fibonacci number in the " + str(y) + "th position.")
		elif y%10 == 2:
			print("The number " + str(n) + " is a Fibonacci number in the " + str(y) + "th position.")
		elif y%10 == 3:
			print("The number " + str(n) + " is a Fibonacci number in the " + str(y) + "th position.")
		else:
			print("The number " + str(n) + " is a Fibonacci number in the " + str(y) + "th position.")
	else:
		print("The number " + str(n) + " is not a Fibonacci number.")

def readAnswer(answer):
	answer = int(answer)
	if answer != 1 and answer != 2 and answer != 3:
		print("Wrong Input")
		exit()
	n = int(input("Enter the necessary number to compute: "))
	if answer == 1:
		print()
		print("This will display the fibonacci series upto the " + str(n) + "th term...")
		displayFibonacciSeries(n)
	elif answer == 2:
		print()
		print("The " + str(n) + "th term in the fibonacci sequence is: " + str(fibonacci(n)))
	else:
		print()
		print("This will show if your number is in the Fibonacci series...")
		checkFibonacciNumber(n)


if __name__ == '__main__':
	beginProgram()
	print()
	userInput = int(input("Enter your choice: "))
	readAnswer(userInput)
