from brain_games.engine import play_game
from brain_games.games.brain_gcd import game_logic


def main():
    task_description = 'Find the greatest common divisor of given numbers.'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
