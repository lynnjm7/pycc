#!/usr/bin/env python3

import argparse

import CreditCardValidation
import CreditCardValidationException as ccve

def getCommandLineArgs():
    """ Process the command line arguments """
    parser = argparse.ArgumentParser(prog="ccvalidator",
            description="Validate and determine the issuer of a given credit card number")
    parser.add_argument("card_num", help="Credit card number")

    return parser.parse_args()

def main():
    try:
        args = getCommandLineArgs()
        creditCard = CreditCardValidation.CreditCard(args.card_num)
        if creditCard.validate():
            print("VALID credit card number")

        print(creditCard.getIssuer().name)
    except ccve.CreditCardValidationException as error:
        print(error)


if __name__ == "__main__":
    main()

