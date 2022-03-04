import numpy as np

lineList = [line.rstrip('\n') for line in open('data.txt')]

testCases = int(lineList[0])
lineList.pop(0)

def read_data():
	tests, counter = {}, 0
	for i in range(1, testCases+1):
		for j in range(int(lineList[0])):
			tests["Case #{0}:".format(i)] = lineList[1:int(lineList[0])+1]

		del lineList[0:int(lineList[0])+1]
	return tests

def working_list(dictionary, key):
	first_lst = dictionary[key]
	final_lst, duplicates = [], 0

	for item in first_lst:
		sentence = []
		final_lst.append(sentence)
		for i in item.split():
			sentence.append(int(i))
	return(final_lst)

def trace_of_matrix(list_used):
	numpy_matrix = np.asarray(list_used)
	return np.trace(numpy_matrix)

def repeating_in_columns(list_used):
	repeated_columns = 0
	new_list = list(map(list, zip(*list_used)))
	for i in new_list:
		if len(i) != len(set(i)):
			repeated_columns += 1
	return repeated_columns

def repeating_in_rows(list_used):
	repeated_rows = 0
	for i in list_used:
		if len(i) != len(set(i)):
			repeated_rows += 1
	return repeated_rows

final_dict = read_data()
for i in range(0, testCases):
	polished_list = working_list(final_dict, list(final_dict.keys())[i])
	trace = trace_of_matrix(polished_list)
	rows = repeating_in_rows(polished_list)
	columns = repeating_in_columns(polished_list)
	print(list(final_dict.keys())[i], trace, rows, columns)
