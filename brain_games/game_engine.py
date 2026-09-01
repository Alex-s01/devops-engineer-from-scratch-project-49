import prompt
from brain_games.cli import welcome_user


def engine(game_module):
    name = welcome_user()
    print(game_module.DESCRIPTION)

    for _ in range(3):
        question, right_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").lower()

        if user_answer == right_answer:
            print("Correct!")
        else:
            print(
                    f"'{user_answer}' is wrong answer ;(. "
                    f"Correct answer was '{right_answer}'."
                    )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
    return
