class MissingOperator(Exception):
    name = 'MissingOperator'

class EmptyPF(Exception):
    name = 'EmptyPF'

class InvalidPF(Exception):
    name = 'InvalidPF'

class InputTooLong(Exception):
    name = 'InputTooLong'

class UnbalancedParens(Exception):
    name = 'UnbalancedParens'
    def __init__(self, numParens):
        self.parens = 'too many ' + '(' if numParens > 0 else ')'
        Exception.__init__(self)

class InvalidChar(Exception):
    name = 'InvalidChar'
    def __init__(self, char):
        self.invalidChar = char
        Exception.__init__(self)

def GenericHandler(func, *args):
    def nested(*args):
        try:
            return func(*args)
        except Exception as error:
            try:
                print('error: ' + error.name)
                raise
            except TypeError:
                print('Unexpected Non-user Error')
    return nested
