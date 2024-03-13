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


def question_gen(ans_input="x = "):
    list = []

    expo = random.randint(0, 5)
    base = random.randint(2, 10)
    argument = base ** expo

    list.append(expo)
    list.append(base)
    list.append(argument)

    unknown = random.choice(list)

    if unknown == argument:
        quiz = f"log{base}(x) = {expo}" \
               f"\n{ans_input}"

        x = argument

    elif unknown == base:
        quiz = f"logx({argument}) = {expo}" \
               f"\n{ans_input}"

        x = base

    else:
        quiz = f"log{base}({argument}) = x" \
               f"\n{ans_input}"

        x = expo

    return quiz, x


# main routine

while True:

    quiz_1 = question_gen()
    ans_1 = quiz_1[1]
    ques_1 = int_check(quiz_1[0])

    if ques_1 == ans_1:
        print("Correct")
        break

    elif ques_1 != ans_1:
        print("wrong")
        break

    else:
        print("value error")
        break
