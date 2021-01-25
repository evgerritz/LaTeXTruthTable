#!/usr/bin/env python3
import sys
import readline
from genlatex import genlatex, gentable
from parser import *
from ttable import getvars
from error import InvalidPF

@GenericHandler
def maketable(rawtext, verbose=False):
    validResults = validInput(rawtext)
    if not validResults['failed']:
        listpf = splitByPrecedence(normalizeInput(rawtext))
        if validPF(listpf):
            pfrepr = textrepr(listpf)
            varlst = getvars(pfrepr) 
            table = gentable(listpf, pfrepr, varlst, verbose)
            latextable = genlatex(pfrepr, listpf, varlst, table, verbose)
            return latextable
        else:
            raise InvalidPF()
    else:
        raise validResults['error']


if __name__ == '__main__':
    def interactive():
        msgs = [' LaTeX Truth Table', 'q or Ctrl-C to quit ']
        msglength = len(msgs[0]) + len(msgs[1])
        sep = '=' * 100 + '\n'
        print('\n' + msgs[0] + ' ' * (len(sep[:-1]) - msglength) + msgs[1])
        try:
            while True:
                print(sep)
                response  = input('Enter PF: ')
                verbose = input('Verbose? (y/N): ') in ['Y', 'y']
                if response.lower() in ['q', 'quit()', 'exit()', 'exit', 'quit']:
                    sys.exit(0)
                table = maketable(response, verbose)
                print(table)
        except KeyboardInterrupt:
            sys.exit(0)
     
    if len(sys.argv) == 1:
        interactive()
    else:
        verbose = True if sys.argv[1] in ('--verbose', '-v') else False
        for arg in sys.argv[(2 if verbose else 1):]:
            print(maketable(arg, verbose))
