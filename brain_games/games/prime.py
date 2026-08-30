import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return "no"

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "no"

    return "yes"


def game():
    question = random.randint(1, 100)
    result = {}
    result["Question"] = question
    result["Answer"] = is_prime(question)

    return result
