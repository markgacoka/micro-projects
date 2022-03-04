'''
Write a function toWeirdCase that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.
The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''

def to_weird_case(string):
    words = string.split(' ')
    result = ''
    for counter, i in enumerate(words):
        for count, j in enumerate(i):
            if count == 0 or count % 2 == 0:
                result += j.upper()
            else:
                result += j.lower()
        if len(words) > 1 and counter < len(words)-1:
            result += ' '
    return(result)