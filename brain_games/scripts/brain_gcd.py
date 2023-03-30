import random
from brain_games.engine import play_game
from math import gcd


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    return f'{num1} {num2}', str(correct_answer)


def main():
    task_description = 'Find the greatest common divisor of given numbers.'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()

