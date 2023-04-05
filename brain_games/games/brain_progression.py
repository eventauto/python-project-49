import random


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]
    return progression


def game_logic():
    progression = generate_progression()
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(hidden_value)
