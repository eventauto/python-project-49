import random

task_description = 'What number is missing in the progression?'


MIN_PROGRESSION_START = 1
MAX_PROGRESSION_START = 50
MIN_PROGRESSION_STEP = 2
MAX_PROGRESSION_STEP = 5
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10


def generate_progression(initial_term, common_difference, length):
    progression = [initial_term + i * common_difference for i in range(length)]
    return progression


def hide_element(progression, hidden_index):
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_value


def format_progression(progression):
    return ' '.join(map(str, progression))


def game_logic():
    initial_term = random.randint(MIN_PROGRESSION_START, MAX_PROGRESSION_START)
    common_difference = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)

    progression = generate_progression(initial_term, common_difference, length)
    hidden_index = random.randint(0, len(progression) - 1)
    progression, hidden_value = hide_element(progression, hidden_index)
    question = format_progression(progression)

    return question, str(hidden_value)
