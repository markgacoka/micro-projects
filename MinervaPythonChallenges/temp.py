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
