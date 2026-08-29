from brain_games.game_engine import engine
from brain_games.games import calc


def main():
    engine(calc.game, calc.DESCRIPTION)


if __name__ == "__main__":
    main()
