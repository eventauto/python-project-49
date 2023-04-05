import random
from math import gcd


def game_logic():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    return f'{num1} {num2}', str(correct_answer)