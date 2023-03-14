import random
from brain_games.cli import welcome_user, greetings

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_number() -> int:
    return random.randint(1, 100)

def play_game():
    greetings()
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = generate_number()
        correct_answer = 'yes' if is_prime(number) else 'no'
        user_answer = input(f"Question: {number}\nYour answer: ")
        if user_answer == correct_answer:
            counter += 1
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")

def main():
    play_game()

if __name__ == '__main__':
    main()
