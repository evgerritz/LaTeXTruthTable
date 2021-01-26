class UserException(Exception): pass

class MissingOperator(UserException):
    name = 'MissingOperator'

class EmptyPF(UserException):
    name = 'EmptyPF'

class InvalidPF(UserException):
    name = 'InvalidPF'

class InputTooLong(UserException):
    name = 'InputTooLong'

class MissingOperands(UserException):
    name = 'MissingOperands'

class UnbalancedParens(UserException):
    name = 'UnbalancedParens'
    def __init__(self, numParens):
        self.parens = 'too many ' + ('(' if numParens > 0 else ')')
        Exception.__init__(self)

class InvalidChar(UserException):
    name = 'InvalidChar'
    def __init__(self, char):
        self.invalidChar = char
        Exception.__init__(self)

