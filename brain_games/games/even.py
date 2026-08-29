import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    result = {}
    number = random.randint(1, 100)
    result["Question"] = number
    result["Answer"] = "yes" if number % 2 == 0 else "no"
    return result
