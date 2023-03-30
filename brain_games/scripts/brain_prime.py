import random
from brain_games.engine import play_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def game_logic():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return number, correct_answer


def main():
    task_desc = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(game_logic, task_desc)


if __name__ == '__main__':
    main()
