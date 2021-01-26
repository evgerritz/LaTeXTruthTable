#!/usr/bin/env python3
import sys
import readline
from genlatex import genlatex, gentable
from parser import *
from ttable import getvars
from error import InvalidPF, UserException

def maketable(rawtext, verbose=False):
    isValid = isValidInput(rawtext)
    if not isValid['failed']:
        listpf = splitByPrecedence(normalizeInput(rawtext))
        if validPF(listpf):
            pfrepr = textrepr(listpf)
            varlst = getvars(pfrepr) 
            table = gentable(pfrepr, len(varlst), verbose)
            latextable = genlatex(pfrepr, listpf, varlst, table, verbose)
            return latextable
        else:
            raise InvalidPF()
    else:
        raise isValid['error']


if __name__ == '__main__':
    def interactive():
        msgs = [' LaTeX Truth Table', 'Ctrl-C to quit ']
        msglength = len(msgs[0]) + len(msgs[1])
        sep = '=' * 100 + '\n'
        print('\n' + msgs[0] + ' ' * (len(sep[:-1]) - msglength) + msgs[1])
        while True:
            try:
                print(sep)
                response  = input('Enter PF: ')
                verbose = input('Verbose? (y/N): ') in ['Y', 'y']
                table = maketable(response, verbose)
                print(table)
            except InvalidChar as error:
                print('error:',  error.name + ':', error.invalidChar)
            except UnbalancedParens as error:
                print('error:',  error.name + ':', error.parens)
            except UserException as error:
                print('error:', error.name)
            except KeyboardInterrupt:
                sys.exit(0)
     
    if len(sys.argv) == 1:
        interactive()
    else:
        verbose = True if sys.argv[1] in ('--verbose', '-v') else False
        for arg in sys.argv[(2 if verbose else 1):]:
            print(maketable(arg, verbose))
