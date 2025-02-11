from games.hi import HiGame
from games.world import WorldGame
from libs.game_manager import GameManager


def main():
    """
    The Main Function. Ideally, just add games here, and run the thing
    """
    game_manager = GameManager()

    game_manager.add_game("hello", HiGame());
    game_manager.add_game("world", WorldGame());
    game_manager.start("hello")

    game_manager.run()

if __name__ == "__main__":
    main()
