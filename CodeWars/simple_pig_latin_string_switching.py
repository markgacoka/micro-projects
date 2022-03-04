'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    words = text.split(' ')
    for count, i in enumerate(words):
        if words[count] == '!' or words[count] == '?' or words[count] == '.':
            continue
        words[count] = words[count][1:] + words[count][0]
        words[count] += 'ay'
    return ' '.join(words)