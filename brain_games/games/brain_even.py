import random

task_description = 'Answer "yes" if the number is even, otherwise answer "no".'


MIN_NUMBER = 1
MAX_NUMBER = 100

def is_even(num):
    return num % 2 == 0

def game_logic():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer
