import sys
import pygame
from pygame.locals import (
    QUIT
)
from libs.game import Game

class GameManager:
    screen_height: int = 800;
    screen_width: int = 800;

    screen: pygame.Surface;
    clock: pygame.Clock;

    running: bool = False;

    current_game: str | None = None;
    games: dict[str, Game] = {};

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()

    def add_game(self, name: str, game: Game):
        if not name:
            raise Exception("No Such Game Exists") 

        self.games.update({
            name: game
        });

    def game_exists(self, name: str) -> bool:
        return name in self.games

    def get_active_game(self) -> Game | None:
        return self.games.get(self.current_game) if self.current_game else None

    def stop(self):
        active = self.get_active_game();
        if active:
            self.current_game = None
            active.stop()


    def start(self, name: str):
        if (not self.game_exists(name) or self.current_game == name):
            return

        self.stop()
        self.current_game = name
            

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    self.running = False

            active_game = self.get_active_game()
            if active_game:
                active_game.render(self.screen)
                active_game.update(events, self, self.screen)

            pygame.display.flip();
            self.clock.tick(60);
        
        pygame.quit();
        sys.exit();

