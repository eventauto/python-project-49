from brain_games.cli import welcome_user, greetings

ROUNDS_COUNT = 3

def play_game(game_logic, task_desc, rounds=ROUNDS_COUNT):
    greetings()
    user_name = welcome_user()
    print(task_desc)

    correct_answers = 0
    while correct_answers < rounds:
        question, correct_answer = game_logic()
        print(f'Question: {question}')
        user_answer = input('Your answer: ').strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
