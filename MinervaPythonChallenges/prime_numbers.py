#Q4. Input takes an integer and lists all the prime numbers below it
def prime_num_finder(num):
	#Try exception used to test if number is input.
	try:
		num = int(num)
	except ValueError:
		print("Input must be a number!")
		exit()
	#We know that all numbers are divisible by 1 so we do not include it
	'''We assume a number is a prime until proven otherwise. For all the numbers
	below the given number, check all the numbers below it if they are divisible by any other number'''
	prime_numbers = []
	for i in range(2, num+1):
		isNumPrime = True
		for j in range(2, i):
			if i%j == 0:
				isNumPrime = False
		if isNumPrime:
			prime_numbers.append(i)
	#One-line if-else clause stating if the list 'prime_numbers' is empty, print None
	print(None) if len(prime_numbers) == 0 else print(prime_numbers)

if __name__=='__main__':
	num1 = prime_num_finder(5)
	num2 = prime_num_finder(1)
