import random
from math import gcd

task_description = 'Find the greatest common divisor of given numbers.'


MIN_NUMBER = 1
MAX_NUMBER = 100

def game_logic():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = gcd(num1, num2)
    return f'{num1} {num2}', str(correct_answer)

