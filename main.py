import readline
from genlatex import genlatex, gentable
from parser import *
from ttable import getvars
from error import InvalidPF

def maketable(rawtext):
    if validInput(rawtext)[0]:
        listpf = splitByPrecedence(normalizeInput(rawtext))
        if validPF(listpf):
            pfrepr = textrepr(listpf)
            varlst = getvars(pfrepr) 
            table = gentable(listpf, pfrepr, varlst)
            latextable = genlatex(pfrepr, listpf, varlst, table)
            return latextable
        else:
            raise InvalidPF()

if __name__ == '__main__':
    while True:
        table = maketable(input('Enter PF: '))
        print(table)


     
