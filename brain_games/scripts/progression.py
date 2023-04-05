from brain_games.engine import play_game
from brain_games.games.brain_progression import game_logic


def main():
    task_description = 'What number is missing in the progression?'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
