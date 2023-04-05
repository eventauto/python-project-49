import random


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    res = eval(expression)
    return expression, str(res)
