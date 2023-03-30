import random
from brain_games.engine import play_game


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    res = eval(expression)
    return expression, str(res)


def main():
    task_description = 'What is the result of the expression?'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
