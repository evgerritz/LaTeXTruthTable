import readline
from genlatex import genlatex, gentable
from parser import *
from ttable import getvars
from error import InvalidPF

@GenericHandler
def maketable(rawtext):
    validResults = validInput(rawtext)
    if not validResults['failed']:
        listpf = splitByPrecedence(normalizeInput(rawtext))
        if validPF(listpf):
            pfrepr = textrepr(listpf)
            varlst = getvars(pfrepr) 
            table = gentable(listpf, pfrepr, varlst)
            latextable = genlatex(pfrepr, listpf, varlst, table)
            return latextable
        else:
            raise InvalidPF()
    else:
        raise validResults['error']


if __name__ == '__main__':
    while True:
        table = maketable(input('Enter PF: '))
        print(table)


     
