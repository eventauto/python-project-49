import random
from brain_games.engine import play_game


def is_even(num):
    return num % 2 == 0


def game_logic():
    num = random.randint(1, 100)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def main():
    task_description = (
        'Answer "yes" if given number is prime. '
        'Otherwise answer "no".')
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
