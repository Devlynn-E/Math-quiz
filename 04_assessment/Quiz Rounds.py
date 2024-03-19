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
        error = (f"Please enter an integer that is "
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

    expo = random.randint(1, max_expo)
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

        This is a quiz based on logarithms
        
        How logs work:
        
        There are three parts of a log; base, exponent and argument
        
        -   base is the number that has an exponent on it such as A in: A^b = c
        -   exponent is the power of the base such as b in: A^b = c
        -   argument is what the base to power of the exponent is equal to, such as c in: A^b = c
        
        All of this can be written in log form. This is what is looks like in log form: logA (c) = b
        
        
        The default parameters of this game are: max base = 10, max exponent = 5
        
        You can edit these by not choosing to use the default parameters, however i wouldn't go too high.
        Otherwise your questions might get a little difficult.
        
        I would only recommend going to a max base of 12 and maybe a max exponent of 6 if your up to it.
        
        🎂🎂🎂Good Luck🎂🎂🎂

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

# asks user if they want to use the default questions
default_params = yes_no("\nDo you want to use the default log parameters? ")

if default_params == "no":
    # asks for the max base and exponent for the questions
    base_input = int_check("\nmax base? ", low=2)
    expo_input = int_check("\nmax exponent? ", low=1)
    print()

else:
    print("\nHighest Base number: 10 | Highest Exponent: 5")
    print()
    base_input = 10
    expo_input = 5

# game loop starts
while rounds_played < rounds_to_play:

    # round heading
    if mode == "infinite":
        heading = f"\n♾♾♾ Question {rounds_played + 1} (infinite mode) ♾♾♾"

    else:
        heading = f"\n📊📊📊 Question {rounds_played + 1} of {rounds_to_play} 📊📊📊"

    print(heading)

    quiz_1 = question_gen("x = ", base_input, expo_input)
    ans_1 = quiz_1[1]
    ques_1 = int_check(quiz_1[0], None, None, "x")

    if ques_1 == "x":
        break

    elif ques_1 == ans_1:
        print("Correct")

    else:
        print("wrong")

    rounds_played += 1
