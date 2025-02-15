import sys
import pygame
from pygame.locals import (
    QUIT
)
from libs.game import Game

class GameManager:
    """
    The Games Manager. This manages which game to load, which game to run, 
    how to run, and when to run.
    It also takes care of initializing pygame, and everything.
    """
    screen_height: int = 800;
    screen_width: int = 800;

    screen: pygame.Surface;
    clock: pygame.Clock;

    running: bool = False;

    current_game: str | None = None;
    games: dict[str, Game] = {};

    def __init__(self) -> None:
        """
        Initializes pygame
        """
        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()

    def add_game(self, name: str, game: Game):
        """
        Adds a game to the Game Manager.
        """
        self.games.update({
            name: game
        });

    def game_exists(self, name: str) -> bool:
        """
        Checks if a game of given name exists
        """
        return name in self.games

    def get_active_game(self) -> Game | None:
        """
        Gets the currently running game, mainly used internally
        """
        return self.games.get(self.current_game) if self.current_game else None

    def stop(self):
        """
        Stops current game from running
        """
        active = self.get_active_game();
        if active:
            self.current_game = None
            active.stop()


    def start(self, name: str):
        """
        Starts a game, with the given name, use this to switch between games
        """
        if (not self.game_exists(name) or self.current_game == name):
            return

        self.stop()
        self.current_game = name
        active = self.get_active_game()
        if active:
            active.init(self.screen)
            

    def run(self):
        """
        The Game Loop. This has checks for events, renders stuff on screen and updates them.
        """
        # active_game = self.get_active_game()
        # if active_game:
        #     active_game.init()

        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    self.running = False

            # Check if there's a current game, and then render and update frames of the game
            active_game = self.get_active_game()
            if active_game:
                active_game.render(self.screen)
                active_game.update(events, self, self.screen)

            # Refresh the screen
            pygame.display.flip();
            # Set the FPS
            self.clock.tick(60);
        
        # Exit if the loop stops
        pygame.quit();
        sys.exit();

