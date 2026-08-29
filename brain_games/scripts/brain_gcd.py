from brain_games.game_engine import engine
from brain_games.games import gcd


def main():
    engine(gcd.game, gcd.DESCRIPTION)


if __name__ == "__main__":
    main()
