from prettytable import PrettyTable

print("Enter your logical statement e.g. (a and b) implies c / ¬a ↔ b v c / a biconditional b")
inputt = input("\n **Ensure there is space between the atomic sentences and the connectives!**\n> ")
inp = inputt.lower()

def user_input():
    global inp
    for n, i in enumerate(inp):
        if i == "&" or i == "&&" or i == "^":
            inp = inp.replace("&" or "&&" or "^", "and")
        elif i == "→" or i == "implication":
            inp = inp.replace("→" or "implication","implies")
        elif i == "↔" or i == "xnor":
            inp = inp.replace("↔" or "xnor","biconditional")
        elif i == "v":
            inp = inp.replace("v" ,"or")
        elif i == "¬":
            i.split("¬")
            inp = inp.replace("¬", "not ")
        else:
            continue
    print("\nThis is your input: " + inp)
    return str(inp)

def get_atomic_sentences():
    global inp
    char_set = ["and", "or", "implies", "biconditional", "&", "&&", "v", "^", "→", "↔", "xnor", "(", ")", "not", "¬"]
    atomic_sentences = []
    input1 = ''.join(c for c in inp if c not in '()')
    input2 = input1.split(" ")
    unique = set(input2)
    unique = list(unique)
    for i in unique:
        if i not in char_set:
            atomic_sentences.append(i)
    atomic_sentences.sort()
    return list(atomic_sentences), input2

def nextprevword(target, source):
    for i, w in enumerate(source):
        if w == target:
            last = ','.join(source[i+1:])
            last = last.replace(",", " ")

            first = ','.join(source[:i])
            first = first.replace(",", " ")
            return first, last
        
def return_value(answer): #list
    global inp
    atomic_dict, input2 = get_atomic_sentences()
    for n, i in enumerate(atomic_dict):
        exec(i + f" = {answer[n]}")
    if 'implies' in inp:
        previous, after = nextprevword('implies', input2)
        input2 = not previous or after
        evaluation = eval(inp)
    elif 'biconditional' in inp:
        previous, after = nextprevword('biconditional', input2)
        if(previous == after): 
            evaluation = True
        else: 
            evaluation = False
    else:
        evaluation = eval(inp)
    return evaluation

def printTruthTable():
    inp = user_input()
    atomic_dict, input2 = get_atomic_sentences()
    x = PrettyTable([n for n in atomic_dict + [str(inp)]])
    p = len(atomic_dict)
    print("Your logical statement has " + str(p) + " atomic sentences.")

    def permutation(n):
        if n < 1:
            return [[]]
        subtable = permutation(n-1)
        return [row + [v] for row in subtable for v in [True,False]]

    truth_table = permutation(p)
    for i in range(2**p):
        x.add_row(truth_table[i] + [return_value(truth_table[i])])
    print(x)

printTruthTable()