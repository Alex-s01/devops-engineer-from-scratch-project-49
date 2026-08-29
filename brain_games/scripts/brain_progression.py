from brain_games.game_engine import engine
from brain_games.games import progression


def main():
    engine(progression.game, progression.DESCRIPTION)


if __name__ == "__main__":
    main()
