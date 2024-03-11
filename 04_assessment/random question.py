import random


import math


# checks that a number is an integer
def int_check(question, low=None, high=None, exit_code=None):

    # if any int is allowed
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is"
                 f"more than / equal to {low}")

    # if the number needs to be between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for inf mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check the int is not low
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# main routine
