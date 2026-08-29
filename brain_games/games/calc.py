import random


DESCRIPTION = "What is the result of the expression?"

def game():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    exp_type = random.choice(("+", "-", "*"))
    result = {}

    match exp_type:
        case "+":
            result["Question"] = f"{number_one} + {number_two}"
            result["Answer"] = str(number_one + number_two)
        case "-":
            result["Question"] = f"{number_one} - {number_two}"
            result["Answer"] = str(number_one - number_two)
        case "*":
            result["Question"] = f"{number_one} * {number_two}"
            result["Answer"] = str(number_one * number_two)

    return result
