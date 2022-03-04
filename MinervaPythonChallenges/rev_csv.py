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

