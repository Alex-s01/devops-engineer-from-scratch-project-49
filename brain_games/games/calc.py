import random

DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    exp_type = random.choice(("+", "-", "*"))

    match exp_type:
        case "+":
            question = f"{number_one} + {number_two}"
            answer = str(number_one + number_two)
        case "-":
            question = f"{number_one} - {number_two}"
            answer = str(number_one - number_two)
        case "*":
            question = f"{number_one} * {number_two}"
            answer = str(number_one * number_two)

    return question, answer
