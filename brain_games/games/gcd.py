import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def calc_gcd(one, two):
    while two != 0:
        one, two = two, one % two
    return one


def game():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    result = {}

    result["Question"] = f"{number_one} {number_two}"
    result["Answer"] = f"{calc_gcd(number_one, number_two)}"

    return result
