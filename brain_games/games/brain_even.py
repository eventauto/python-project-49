import random


def is_even(num):
    return num % 2 == 0


def game_logic():
    num = random.randint(1, 100)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer
