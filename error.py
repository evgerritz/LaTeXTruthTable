class MissingOperator(Exception):
    name = 'MissingOperator'

class EmptyPF(Exception):
    name = 'EmptyPF'

class InvalidPF(Exception):
    name = 'InvalidPF'

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
