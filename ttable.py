testEXP = "(p AND q) OR (NOT r)"
testBS = "010"

OPS = ['AND', 'OR', 'XOR', 'NOT', 'IMPLIES', 'IFF'] 

def offset(string):
    return string + " "
def deoffset(string):
    return string[:-1]

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

#returns a list of all possible bit strings of length numVars
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

#substitute values into exp
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


def splitrest(exp):
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
            exp = exp[0:i] + 'NULL' + exp[i+1:]
        i+=1
    return exp.split('NULL')

def parenstolist(exp):
    lst = []
    blocks = splitrest(exp)
    if not blocks:
        return None                     #UNBALANCED PARENS
    for block in blocks:
        if block[0] == '(':
            block = parenstolist(block[1:-1])
        lst.append(block)
    return lst

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

#expects prefix-notation list representing a boolean exp
# with truth values substituted
def evalbool(exp):
    OP = exp[0]
    if exp == '0':
        return 0
    elif exp == '1':
        return 1
    elif OP == 'NOT':
        Rresult =  evalbool(exp[1])
        Lresult =  NOT(Rresult)
        return Lresult
    elif OP in OPS:
        Lresult =  evalbool(exp[1])
        Rresult =  evalbool(exp[2])
        Mresult = eval(OP)(Lresult, Rresult)
        return Mresult
    else:
        return None

def isNested(lst):
    return any(isinstance(i, list) for i in lst)

def combineevals(exp):
    OP = exp[0]
    if type(exp) is not list:
        return None
    elif not isNested(exp):
        return str(evalbool(exp))
    elif OP == 'NOT':
        Rresult =  str(evalbool(exp[1]))
        Lresult =  evalbool(['NOT', Rresult])
        return str(Lresult) + str(combineevals(exp[1]))
    elif OP in OPS:
        Lresult =  str(evalbool(exp[1]))
        Rresult =  str(evalbool(exp[2]))
        Mresult =  str(evalbool([OP, Lresult, Rresult]))

        tempLeft = combineevals(exp[1])
        tempRight = combineevals(exp[2])
        
        if tempLeft:
            Mresult = str(tempLeft) + Mresult
        if tempRight: 
            Mresult += str(tempRight)

        return Mresult
    else:
        return None

def genttable(exp):
    varlst = getvars(exp)
    inputs = binarycount(len(varlst))
    print(str(varlst)+'|'+exp)
    for binstr in inputs:
        temp = makeprefix(parenstolist(sub_into_exp(exp, binstr)))
        result = combineevals(temp)
        print(binstr + '|' + result)
    return None
    genttable(exp)
