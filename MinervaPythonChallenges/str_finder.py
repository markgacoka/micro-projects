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

