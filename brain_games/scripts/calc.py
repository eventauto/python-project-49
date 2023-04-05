from brain_games.engine import play_game
from brain_games.games.brain_calc import game_logic


def main():
    task_description = 'What is the result of the expression?'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
