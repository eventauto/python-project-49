from brain_games.engine import play_game
from brain_games.games.brain_prime import  game_logic


def main():
    task_description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
