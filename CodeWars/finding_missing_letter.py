'''
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
'''


def find_missing_letter(chars):
    bool = False
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    if chars[0].isupper():
        bool = True
    for count, i in enumerate(chars):
        chars[count] = i.lower()
    start_index = alphabet.index(chars[0])
    end_index = alphabet.index(chars[-1])
    full_lst = alphabet[start_index:end_index]
    difference = [x for x in full_lst if x not in chars]
    if bool:
        return difference[0].upper()
    else:
        return difference[0]