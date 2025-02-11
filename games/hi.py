from typing import override

import pygame
from pygame.locals import K_RIGHT
from libs.game import Game
from libs.game_manager import GameManager

class HiGame(Game):
    rect: pygame.Surface = pygame.Surface((50, 50))

    @override
    def init(self):
        pass

    @override
    def render(self, screen: pygame.Surface):
        self.rect.fill((255, 0, 0))
        screen.blit(self.rect, pygame.Rect(20, 20, 50, 50))
        pass

    @override
    def update(self, events: list[pygame.Event], manager: GameManager, screen: pygame.Surface):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                manager.start("world")

    @override
    def stop(self):
        pass
