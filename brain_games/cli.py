def greetings():
    print("Welcome to the Brain Games !")


def welcome_user():
    # prompt.string(prompt='May I have your name?')
    user_name = input('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name

if __name__ == '__main__':
    welcome_user()
