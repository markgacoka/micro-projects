# Python-Challenges
Python Code for Solved Challenges

### Challenge 1
A function called str_finder(lst) that accepts a list as an argument and returns a list containing every string element. If the list does not contain any string elements, the function should return None.

### Challenge 2
A function called fah_to_cel_converter(degrees) that takes Fahrenheit degrees as parameter and returns it converted to Celsius degrees rounded to 2 decimal places.

### Challenge 3
[CSV file:](https://github.com/markgacoka/Python-Challenges/blob/master/coffeeshops%20-%20Sheet1.csv)

Coffee shops                   |  Average Daily Revenue
-------------------------------|-----------------------
Coffee Cultures                |  1300
sightglass coffee              |  1345
flywheel coffee roasters       |  1097
blue bottle                    |  987
starbucks                      |  2356
ritual roasters coffee         |  1029
Equator Coffees & Teas         |  1567
Tartine Manufactory            |  2039
Sightglass Coffee              |  2790
Caffe Trieste                  |  2384
George and Lennie              |  1307
Linea Caffe                    |  1289
Saint Frank                    |  1038
Wrecking Ball Coffee Roasters  |  876
hearth                         |  1567
the buena vista                |  3647
cento                          |  1390
vervo coffee                   |  1098


The .csv file contains the hypothetical data of daily revenues of coffee shops located in San Francisco. 
Write a function sum_revenue() that downloads this data into your program and finds the total revenue of all coffeeshops. Your function should not receive arguments and should find the sum by iterating through the numbers in the second column of the file. No external libraries can be used. You should check your result by comparing it to the sum returned by using the built-in sum function.
* Return a tuple in the format (sum, boolean)

### Challenge 4
A function called prime_num_finder(num) that takes an integer as a parameter and returns a list containing all prime numbers that are smaller or equal to this parameter or None otherwise.

### Challenge 5
Write a simulation of the Dice Game. The rules of the game are as follows:
* a. There are at least 2 players and at most 4
* b. Each player takes a turn and rolls one standard dice; The number on a dice is added to his score
* c. Whoever first accumulates exactly 23 points wins
* d. If the player accumulates more than 23 points, then his score becomes 0.
* e. If more than 1 player accumulates exactly 23 points in the same turn, then the game ends in a tie, and all players with 23 points win.

Your program should produce a line graph that shows the players’ running scores after each turn.

### Challenge 6
Brownian motion.

Write a function my_particle(n) to simulate this movement of one particle in 2D space using Python. The function should accept one argument, n, the number of moves your particle makes (1 < n < 10 000). Choose your own starting point and sizes of steps. The function should output a visualization of the path that the particle takes, like the one below, and print the distance between start and end point.
