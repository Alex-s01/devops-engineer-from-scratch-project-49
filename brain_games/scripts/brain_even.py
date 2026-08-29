import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ").capitalize()
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    counter = 0
    
    while True:
        number = random.randint(1, 100)
        even = "yes" if number % 2 == 0 else "no"
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ").lower()
        if answer == even:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{even}'.")
            print(f"Let's try again, {name}!")
            return
        if counter == 3:
            print(f"Congratulations, {name}!")
            return

if __name__ == "__main__":
    main()
