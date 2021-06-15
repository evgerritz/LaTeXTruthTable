from src.ttable import splitBlocks, OPS, SYMBOLIC_OPS, containsNested, BINARY_OPS
from src.error import MissingOperator, EmptyPF, UnbalancedParens, InputTooLong, InvalidChar 

PRECEDENCE = {'AND':2, 'OR':4, 'XOR':3, 'NOT':1, 'IMPLIES':5, 'IFF':5, 'NOR':3, 'NAND':3, 'LOWEST':0}

def isValidChar(char):
    return char.isalpha() or char in ['0','1', '(', ')', ' '] + list(''.join(SYMBOLIC_OPS.keys()))

def isValidLength(string):
    return len(string) < 100 

def numUnbalancedParens(string):
    return string.count('(')-string.count(')')

def isValidInput(string):
        #input too long!
    if not isValidLength(string):
        return {'failed': True, 'error':InputTooLong()}
    for char in string:
        if not isValidChar(char):
            return {'failed':True, 'error':InvalidChar(char)}
    parens = numUnbalancedParens(string)
    if parens != 0:
        return {'failed':True, 'error':UnbalancedParens(parens)}
    return {'failed':False}

def normalizeInput(string):
    string = string.strip()
    for op in OPS:
        isntNot = (op != 'NOT')
        string = string.replace(isntNot*' '+op.lower()+' ', isntNot*' ' + op + ' ') 
        string = string.replace(isntNot*' '+op.title()+' ', isntNot*' ' + op + ' ') 
    string = string.replace('<->', 'IFF')
    for op in sorted(SYMBOLIC_OPS):
        if op in ('~', '!', '<>'):
            string = string.replace(op, SYMBOLIC_OPS[op] + ' ')
        else:
            string = string.replace(op, ' ' + SYMBOLIC_OPS[op] + ' ')
    #squish internal whitespace down
    string = ' '.join(string.split())
    return string

def isLowerPrecedence(prec1, prec2):
    return prec1 > prec2

def splitByPrecedence(pfstring):
    lowestPrec = {'index': -1, 'val': PRECEDENCE['LOWEST']} 
    splitted = splitBlocks(pfstring)
    if not splitted[0]:
        raise EmptyPF()
    elif len(splitted) == 1:
        if pfstring[0] == '(' and pfstring[-1] == ')':
            return splitByPrecedence(pfstring[1:-1])
        else:
            return pfstring
    else:
        for index, word in enumerate(splitted):
            if word in OPS and isLowerPrecedence(PRECEDENCE[word], lowestPrec['val']):
                lowestPrec = {'index': index, 'val': PRECEDENCE[word]}
        index = lowestPrec['index']
        if index == -1: raise MissingOperator()
        OP = splitted[index]
        left = ' '.join(splitted[:index])
        right = ' '.join(splitted[index+1:])
        if left:
            return [splitByPrecedence(left), OP, splitByPrecedence(right)]
        else:
            return [OP, splitByPrecedence(right)]

def textrepr(listpf):
    if not isinstance(listpf, list):
        return listpf
    if not containsNested(listpf):
        return '(' + ' '.join(listpf) + ')'
    else:
        results = [textrepr(listpf[i]) for i in range(len(listpf))]
        return '(' + ' '.join(results) + ')'

def validPF(listpf):
    if isinstance(listpf, str) and not listpf.upper() in OPS:
        return True
    elif listpf[0] == 'NOT' and len(listpf) == 2:
        return validPF(listpf[1])
    elif listpf[1] in BINARY_OPS and len(listpf) == 3:
        return validPF(listpf[0]) and validPF(listpf[2]) 
    else:
        return False
