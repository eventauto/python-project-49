import random

task_description = 'What is the result of the expression?'


MIN_NUMBER = 1
MAX_NUMBER = 100

def game_logic():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    res = eval(expression)
    return expression, str(res)
