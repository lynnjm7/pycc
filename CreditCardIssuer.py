"""
For details on the implemnentation of the per-issuer
validation rules see https://en.wikipedia.org/wiki/Payment_card_number
"""

class CreditCardIssuer(object):
    """ Base credit card issuer """
    def __init__(self, name = ""):
        self.name = name

    def isIssuer(self, cardNumber):
        """
        Given a credit card number, determine if the number is from the specific issuer
        """
        raise NotImplemented


class AmericanExpress(CreditCardIssuer):
    """ American Express card issuer specialization """
    def __init__(self):
        super().__init__("American Express")

    def isIssuer(self, cardNumber):
        """
        Validate the card against the known American Express rules
        """
        start = cardNumber[0:2]
        if ((start == "34" or start == "37") and len(cardNumber) == 15):
            return True

        return False


class Discover(CreditCardIssuer):
    """ Discover card issuer specialization """
    def __init__(self):
        super().__init__("Discover")

    def isIssuer(self, cardNumber):
        """
        Validate the card against the known Discover Card rules
        """
        start = cardNumber[0:2]
        if (start == "64" or start == "65" or cardNumber[0:4] == "6011") and len(cardNumber) in range(16, 20):
            return True

        return False


class MasterCard(CreditCardIssuer):
    """ MasterCard issuer specialization """
    def __init__(self):
        super().__init__("MasterCard")

    def isIssuer(self, cardNumber):
        """
        Validate the card against the MasterCard known rules
        """
        firstRange =  int(cardNumber[0:2]) in list(range(51, 56))
        secondRange =  int(cardNumber[0:2]) in list(range(2221, 2721))

        if (firstRange or secondRange) and len(cardNumber) == 16:
            return True

        return False



class Visa(CreditCardIssuer):
    """ Visa issuer specialization """
    def __init__(self):
        super().__init__("Visa")

    def isIssuer(self, cardNumber):
        """
        Validate the card against the Visa konwn rules
        """
        lengthSet = set({13, 16, 19})
        if cardNumber[0] == "4" and (len(cardNumber) in lengthSet):
            return True

        return False

