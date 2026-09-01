import random

DESCRIPTION = "What number is missing in the progression?"


def gen_sequence():
    start = random.randint(1, 85)
    step = random.randint(1, 10)
    count = random.randint(5, 12)
    result = []

    for _ in range(count):
        result.append(str(start))
        start += step

    return result


def get_question_and_answer():
    sequence = gen_sequence()
    selected_index = random.choice(range(len(sequence)))
    answer = f"{sequence[selected_index]}"
    sequence[selected_index] = ".."
    question = " ".join(sequence)

    return question, answer
