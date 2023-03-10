import random
from brain_games.cli import welcome_user, greetings


def is_even(num):
    return num % 2 == 0


def even_game():
    greetings()
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer = 0
    while right_answer < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = input('Your answer: ')
        if answer == 'yes' and is_even(num) \
                or answer == 'no' and not is_even(num):
            print('Correct!')
            right_answer += 1
        else:
            correct_answer = 'yes' if is_even(num) else 'no'
            print(f"'{answer}' is wrong answer ;(. "
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')


def main():
    even_game()


if __name__ == '__main__':
    main()
