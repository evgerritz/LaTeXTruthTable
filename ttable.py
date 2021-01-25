OPS = ['AND', 'OR', 'XOR', 'NOT', 'IMPLIES', 'IFF', 'NOR', 'NAND']
NOTINDEX = OPS.index('NOT')
BINOPS = OPS[:NOTINDEX] + OPS[NOTINDEX+1:]
SYMBOLIC_OPS = {'&':'AND', '*': 'AND', '|':'OR', '+':'OR', '^':'XOR', '~':'NOT', '!':'NOT', '<>':'NOT', '=>':'IMPLIES', '->':'IMPLIES', '<=>':'IFF', '<->':'IFF'}

#de/offset: adds and removes a space at the end of a string,
#            for easier parsing of words
def offset(string):
    return string + " "
def deoffset(string):
    return string[:-1]

#getvars: extract all non non-OP strings from exp
def getvars (exp):
    exp = offset(exp)
    varlst = []
    word = ""
    for char in exp:
        if char in [' ', '(', ')']:
            if word and word not in OPS and word not in varlst:
                varlst.append(word)
            word = ""
            continue
        word += char   
    return varlst

#binarycount: returns a list of all possible bit strings of length numVars
def binarycount (numVars):
    if numVars == 1:
        return ['0','1']
    else:
        strs = []
        for binstr in binarycount (numVars - 1):
            strs.append("0" + binstr)
            strs.append("1" + binstr)
        strs.sort()
        return strs

#sub_into_exp: substitute truth values into exp
def sub_into_exp(exp, binstr):
    exp = offset(exp)

    varlst = getvars(exp)
    env = {varlst[i]: int(binstr[i]) for i in range(len(varlst))} 

    word = ""
    for i, char in enumerate(exp):
        if char in [' ', '(', ')']:
            if word and word not in OPS:
                exp = exp[0:i-len(word)] + str(env[word]) + exp[i:] 
            word = ""
            continue
        word += char   
    return deoffset(exp)

#findclosingparen: returns the index in exp of the paren corresponding with
#                  the first character of exp, if that char is indeed a paren
def findclosingparen(exp):
    parencount = 0
    for i, char in enumerate(exp):
        if char == '(':
            parencount += 1
        elif char == ')':
            parencount -= 1

        if parencount == 0:
            return i
    return None

#splitBlocks: splits exp into a list of operators and operands 
def splitBlocks(exp):
    exp = exp.strip()
    i = 0
    while i < len(exp):
        char = exp[i]
        if char == '(':
            split = findclosingparen(exp[i:])
            if not split:
                return None
            i += split
            continue
        elif char == ' ':
               exp = exp[0:i] + 'NULL' + exp[i+1:].lstrip() #skip whitespace
        i+=1
    return exp.split('NULL')

#makeprefix: converts infix notation of user input into prefix notation
def makeprefix(exp):
    lst = []
    if type(exp) is not list:
        return exp
    elif exp[0] == 'NOT':
        lst.append('NOT')
        lst.append(makeprefix(exp[1]))
        return lst
    elif len(exp) == 3: 
        lst.append(exp[1])
        lst.append(makeprefix(exp[0]))
        lst.append(makeprefix(exp[2]))
        return lst
    else:
        return makeprefix(exp[0])

#definitions of operators for evaluation
def AND (a, b):
    return a & b

def OR (a, b):
    return a | b

def XOR (a, b):
    return a ^ b

def NOT (a):
    return ~ a + 2

def IMPLIES (a,b):
    return OR(NOT(a), b)

def IFF(a,b):
    return NOT(XOR(a,b))

def NOR(a,b):
    return NOT(OR(a,b))

def NAND(a,b):
    return NOT(AND(a,b))

#evalbool: returns the truth value of a prefix-notation
#          list representing a PF with truth values substituted
def evalbool(exp):
    op = exp[0]
    if exp == '0':
        return 0
    elif exp == '1':
        return 1
    elif op == 'NOT':
        Rresult =  evalbool(exp[1])
        Lresult =  NOT(Rresult)
        return Lresult
    elif op in BINOPS:
        Lresult =  evalbool(exp[1])
        Rresult =  evalbool(exp[2])
        Mresult = eval(op)(Lresult, Rresult)
        return Mresult
    else:
        return None

#containsNested: returns True if a list contains at least one list
def containsNested(lst):
    return any(isinstance(i, list) for i in lst)

#combineevals: combines the truth values of all nested compound PFs
#               from left to right into one string 
def combineevals(exp, verbose=False):
    OP = exp[0]
    if type(exp) is not list:
        if verbose:
            return exp
        else:
            return None
    elif not containsNested(exp):
        result = str(evalbool(exp)) 
        return result if not verbose else exp[1] + result + exp[2]
    elif OP == 'NOT':
        Rresult =  str(evalbool(exp[1]))
        Lresult =  evalbool(['NOT', Rresult])
        return str(Lresult) + str(combineevals(exp[1], verbose))
    elif OP in OPS:
        Lresult =  str(evalbool(exp[1]))
        Rresult =  str(evalbool(exp[2]))
        Mresult =  str(evalbool([OP, Lresult, Rresult]))

        tempLeft = combineevals(exp[1], verbose)
        tempRight = combineevals(exp[2], verbose)
        
        if tempLeft:
            Mresult = str(tempLeft) + Mresult
        if tempRight: 
            Mresult += str(tempRight)

        return Mresult
    else:
        return None
