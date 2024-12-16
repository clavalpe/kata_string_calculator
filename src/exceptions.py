class NegativeNumbersNotAllowed(Exception):
    def __init__(self):   
        message = 'error: negatives not allowed: -2'
        super().__init__(message)