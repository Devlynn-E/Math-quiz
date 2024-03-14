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


# generates a random logarithm question
def question_gen(ans_input="x = ", max_base=10, max_expo=5):
    list = []

    expo = random.randint(0, max_expo)
    base = random.randint(2, max_base)
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


def instructions():
    print('''

        **** instructions ****

        To begin, choose the number of rounds (or press <enter> for infinite mode).

        You will then chose a lower and higher number (inclusive) that will contain your secret number 

        You will then try to guess the number while the computer will give you hints for each guess

        You will receive statistics on your guesses used and will be able to see your game history at the end of the game

        Type <xxx> to end the game at anytime.

        🎂🎂🎂Good Luck🎂🎂🎂

            ''')


def yes_no(question):
    # starts loop
    while True:
        response = input(question).lower()

        # defines
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes or no")


# main routine

mode = "regular"
rounds_played = 0
end_game = "no"

ans_his = []
response_his = []

print("\n📈📈📈 Math Quiz (Logs) 📉📉📉")
print()

# instructions
wants_instructions = yes_no("Do you want to view the instructions? ")

if wants_instructions == "yes":
    # displays instructions
    instructions()

num_rounds = int_check("\nHow many questions? <enter for infinite>: ", low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    rounds_to_play = 37

else:
    rounds_to_play = num_rounds

default_params = yes_no("\nDo you want to use the default log parameters? ")
if default_params == "no":
    base_input = int_check("\nmax base? ", low=2)
    expo_input = int_check("\nmax exponent? ", low=0)
    print()

else:
    print("\nHighest Base number: 10 | Highest Exponent: 5")
    print()
    base_input = 10
    expo_input = 5

while True:

    quiz_1 = question_gen("x = ", base_input, expo_input)
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
