from CreditCardIssuer import *
from CreditCardValidationException import *

class CreditCard(object):
    """
    A credit card with a given number.
    """
    def __init__(self, cardNumber):
        self.cardNumber = str(cardNumber)

    def validate(self):
        """
        Validates a credit card number and returns True if everything is acceptable
        with the credit card number. Throws a CreditCard Validation exception
        if the validation fails.
        """
        # TODO: For future experiments, this can be refactored to remove the
        #custom exception and return a False boolean flag.
        if self.calculateLuhn(self.cardNumber[0:-1]) == int(self.cardNumber[-1]):
            return True
        raise CreditCardValidationException("Invalid card number")

    def calculateLuhn(self, number):
        """
        Calculate the Luhn algorithm for validating a creit card number. For
        details of this algorithm see:
            https://en.wikipedia.org/wiki/Luhn_algorithm
        """
        rev = list(number[::-1])
        ret = []

        for i in range(len(rev)):
            if i % 2 != 0:
                ret.append(int(rev[i]))
            else:
                ret.append(int(rev[i]) * 2)

        sum = 0
        for i in range(len(ret)):
            if ret[i] > 9:
                sum = sum + (ret[i] - 9)
            else:
                sum = sum + ret[i]

        return sum % 10


    def getIssuer(self):
        """
        Get the issuer of the credit card based on the list of supported (i.e. defined)
        issuer types.

        Throws a credit card validation excpetion if the issuer is unable to be identified.
        """
        issuers = [Visa(), MasterCard(), AmericanExpress(), Discover()]
        for issuer in issuers:
            if issuer.isIssuer(self.cardNumber):
                return issuer

        raise CreditCardValidationException("Unknown Issuer")

