class CreditCardValidationException(Exception):
    """
    Custom exception to let the type system help us with naming
    exceptions generated when processing a credit card number.
    """
    def __init__(self, message):
        super(CreditCardValidationException, self).__init__(message)

