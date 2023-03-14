import random
from brain_games.cli import welcome_user, greetings

def even_game():
    greetings()
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer = 0
    while right_answer < 3:
        num = random.randint(1,100)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        correct_answer = 'yes' if num % 2 == 0 else 'no'
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
        elif answer not in ('yes', 'no'):
            print(f"Incorrect input, please enter 'yes' or 'no', {user_name}")
        else:
            print('Correct!')
            right_answer += 1
    print(f'Congratulations, {user_name}!')


def main():
    even_game()


if __name__ == '__main__':
    main()
