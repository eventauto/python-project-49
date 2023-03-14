import random
from brain_games.cli import welcome_user, greetings

def generate_progression() -> list[int]:
    start = random.randint(1, 50)
    step = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]
    return progression

def play_game():
    greetings()
    user_name = welcome_user()
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        progression = generate_progression()
        hidden_index = random.randint(0, len(progression) - 1)
        hidden_value = progression[hidden_index]
        progression[hidden_index] = '..'
        question = ' '.join(map(str, progression))
        user_answer = input(f"Question: {question}\nYour answer: ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        correct_answer = hidden_value
        if user_answer == correct_answer:
            counter += 1
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
    print(f"Congratulations, {user_name}!")

def main():
    play_game()


if __name__ == '__main__':
    main()