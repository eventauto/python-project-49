import random
from brain_games.cli import welcome_user, greetings

def calc_game():
    greetings()
    user_name = welcome_user()
    print('What is the result of the expression?')
    right_answer = 0
    while right_answer < 3:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        operator = random.choice(['+', '-','*'])
        expression = f'{num1} {operator} {num2}'
        result = eval(expression)
        print(f'Question: {expression}')
        answer = int(input().strip())
        if answer == result:
            print("Correct!")
            right_answer = right_answer + 1
        else:
            print(f"'{answer} is wrong answer ;(. Correct answer was '{result}'. ")
            print(f"Let`s try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")

def main():
    calc_game()

if __name__ == '__main__':
    main()