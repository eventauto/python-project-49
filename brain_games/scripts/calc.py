from brain_games.engine import play_game
from brain_games.games.brain_calc import game_logic, task_description


def main():
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
