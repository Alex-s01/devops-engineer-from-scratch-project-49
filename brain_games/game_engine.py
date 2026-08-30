import prompt


def engine(game, rules: str):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ").capitalize()
    print(f"Hello, {name}!")
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
