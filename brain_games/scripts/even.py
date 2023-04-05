from brain_games.engine import play_game
from brain_games.games.brain_even import game_logic


def main():
    task_description = 'Answer "yes" if the number is even, ' \
                       'otherwise answer "no".'
    play_game(game_logic, task_description)


if __name__ == '__main__':
    main()
