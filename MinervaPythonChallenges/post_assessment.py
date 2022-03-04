'''*************************************************************************************************************************************************************'''
#Q1. Accepts a list then returns every string element
def str_finder(lst):
	str_lst = [] #define an empty string
	#If-else clause checks for the prescence of a string, then loops to print each string found. Else a None is printed
	if any(isinstance(i, str) for i in lst):
		for j in lst:
			if type(j) is str:
				str_lst.append(j)
		print(str_lst)
	else:
		print("None")

if __name__=='__main__':
	str_finder([1.5, "Bob's donuts", 3, True, "17"])
	str_finder([0.05, True, 45, 100**23])
	
'''*************************************************************************************************************************************************************'''
	
#Q2. Convert Farenheit degrees to Celsius using formula
def fah_to_cel_converter(degrees):
	#define the equation and equate it to an integer variable 'celsius' then print out the result
	celsius = 5/9*(degrees - 32)
	celsius = round(celsius, 2)
	print(celsius)

if __name__=='__main__':
	fah_to_cel_converter(3)
	fah_to_cel_converter(90)
	
'''*************************************************************************************************************************************************************'''
	
#Q3. Calculate the sum of a csv column without using other Python libraries. Import required default dependancies
import csv, codecs
from urllib.request import urlopen

def sum_revenue():
	#Define the rul to scrape the csv content, and read its contents then store it to cr
	url = 'https://drive.google.com/uc?export=download&id=1hiPTLgU69boF72-uY8qSytIfrDXVqU_V'
	response = urlopen(url)
	cr = csv.reader(codecs.iterdecode(response, 'utf-8'))
	next(cr)
	#Define 'total' to 0 which will store the total value after increment and 'daily_rev' list that will append the column for easy access
	total, daily_rev = 0, []
	#For each row in the cr csv file, add the values in the 2nd column
	for row in cr:
		total += int(row[1])
		daily_rev.append(int(row[1])) #Appended the column to a list to evade StopIteration Exception
	row_sum = sum(daily_rev)

	#Return tuple that displays the incremented total then compares the two values as a boolean expression
	return (total, total == row_sum)

if __name__=='__main__':
	sum_function = sum_revenue()
	print(sum_function)
	
'''*************************************************************************************************************************************************************'''
	
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
	
'''*************************************************************************************************************************************************************'''
	
#Q5. A Simple Python Dice Game. Import dependencies
import random
import matplotlib.pyplot as plt

def game(players):
	'''Define lists 'player_win' to store win result, 'player_score' to store
	ongoing scores and list 'counter' used as the x-ticks for the graph.
	There is 'player_score' list for the graph and scores dictionary for display'''
	player_win, player_score, counter = [], [], []
	#Nested if - define different dictionaries for each game state. 2 players have 2 key-value pairs. Key is player number, value is score during game
	if players == 2:
		scores = {'1': 0, '2': 0}
	elif players == 3:
		scores = {'1': 0, '2': 0, '3': 0}
	elif players == 4:
		scores = {'1': 0, '2': 0, '3': 0,'4': 0}
	else:
		print("Players must be between 2-4")
		exit()

	#Initialize 'counter_num' that will incrementing each turn and append it to 'counter' list 
	counter_num = 0
	while True:
		counter_num += 1
		counter.append(counter_num)
		'''For each turn, pick a random number as the dice roll,
		add the score to the 'scores' dictionary and if more than 23,
		reduce score to 0, if exactly 23 then
		print out win message stored in 'player_win'. Lastly, append
		the score to the 'player_score' list to be used in the graph'''
		for player in range(1, players+1):
			dice_outcome = random.randint(1, 6)
			scores[str(player)] = dice_outcome + scores.get(str(player))
			if scores[str(player)] > 23:
				scores.update([(str(player), 0)])
			elif scores[str(player)] == 23:
				player_win.append("Player "+str(player)+" won!")
			player_score.append(scores[str(player)])

		'''If a win state is found, end the while loop by printing
		the winners, and plot to graph according to number of players.
		List comprehension is used in the form of list[start:stop:step]'''

		if 23 in list(scores.values()):
			print(scores)
			print(*player_win, sep='\n')
			if players == 2:
				plt.plot(counter, player_score[0::players], color='b')
				plt.plot(counter, player_score[1::players], color='y')
				plt.legend(['Player 1', 'Player 2'], loc='upper left')
			elif players == 3:
				plt.plot(counter, player_score[0::players], color='b')
				plt.plot(counter, player_score[1::players], color='y')
				plt.plot(counter, player_score[2::players], color='g')
				plt.legend(['Player 1', 'Player 2', 'Player 3'], loc='upper left')
			else:
				plt.plot(counter, player_score[0::players], color='b')
				plt.plot(counter, player_score[1::players], color='y')
				plt.plot(counter, player_score[2::players], color='g')
				plt.plot(counter, player_score[3::players], color='r')
				plt.legend(['Player 1', 'Player 2', 'Player 3', 'Player 4'], loc='upper left')
			plt.xlabel("Turns")
			plt.ylabel("Points")
			plt.title("Running Scores", fontsize=15)
			plt.show()
			exit()
		print(scores)

if __name__=='__main__':
	game(3)
	
'''*************************************************************************************************************************************************************'''


#Q6. Simulate and visualize a haphazard moving particle. Import dependancies
'''I believe my approach is algorithmically-efficient because I have incorporated both
the magnitude (number on the number-line) and the direction
(negative or positive) of the particle within my random function. The random
function picks a random number that contains both
a representation of how far it will go on the graph and in which direction.
The range between the negative and positive number is equal and small. Thus, the
movement varies but uniformly within a confined range. With increasing number of steps,
the algorithm becomes efficient because the random function is called only once with each axis.'''

import matplotlib.pyplot as plt
import random, math

def my_particle(n):
	#If the number of steps is greater or less than the stated, produce exception and quit
	max_steps = 10000
	if n < 1 and n > max_steps:
		print("Input value of n greater than 1 but less than 10000")
		exit()

	#Define the value of the origin (x, y) and the lists storing their movements
	x, y = 20, 20
	x_movement, y_movement = [x], [y]
	#Loop through each number of steps appending a random number between -10 and 10. Append it to the movements list
	for point in range(n):
		x += random.randint(-10, 10)
		y += random.randint(-10, 10)
		x_movement.append(x)
		y_movement.append(y)
	return [x_movement, y_movement]

#define an instance of a function
if __name__=='__main__':
	simulation = my_particle(50)
	#define the last positions after all the steps have been completed then calculate the distance between them
	final_x = simulation[0][-1]
	final_y = simulation[1][-1]
	magnitude = round(math.sqrt((20 - final_x)**2 + (20 - final_y)**2), 1)
	print("The distance between the two points is: " + str(magnitude))
	#plot the graph
	plt.title("Random Simulation", fontsize=10)
	plt.plot(simulation[0], simulation[1],  marker='o', color='b')
	plt.show()

'''*************************************************************************************************************************************************************'''
