import random
from brain_games.cli import welcome_user, greetings
import prompt
from math import gcd


def play_game():
    greetings()
    user_name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        user_answer = prompt.integer('Your answer: ')
        correct_answer = gcd(num1, num2)
        if user_answer == correct_answer:
            counter = counter + 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")


def main():
    play_game()


if __name__ == '__main__':
    main()
