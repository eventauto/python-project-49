from brain_games.cli import welcome_user, greetings


def play_game(game_logic, task_description, rounds=3):
    greetings()
    user_name = welcome_user()
    print(task_description)

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