'''
Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''

def maskify(cc):
    new_str = cc[:-4]
    
    if len(cc) == 0:
        return ''
    elif len(cc) < 4:
        return cc
    else:
        cc = ''.join(("#"*(len(cc)-4))) + cc[-4:]
        return cc