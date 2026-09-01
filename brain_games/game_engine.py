import prompt
from brain_games.cli import welcome_user


def engine(game, rules: str):
    name = welcome_user()
    print(rules)

    for _ in range(3):
        session_vars = game()
        print(f"Question: {session_vars.get('Question')}")
        answer = prompt.string("Your answer: ").lower()

        if answer == session_vars.get("Answer"):
            print("Correct!")
        else:
            print(
                    f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{session_vars.get('Answer')}'."
                    )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
    return
