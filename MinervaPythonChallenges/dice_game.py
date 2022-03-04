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
