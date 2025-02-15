from typing import override

import pygame
from pygame.locals import K_RIGHT
from games.tetris.block import Block, TetroMine
from games.tetris.board import Board
from libs.game import Game
from libs.game_manager import GameManager


class Tetris(Game):
    block_size: int = 30
    block_step_delay: int = 30
    vert_items: int = 10
    hor_items: int = 20

    board: Board = Board(block_size, vert_items, hor_items)
    tetromine: TetroMine = TetroMine.random()

    def __init__(self) -> None:
        super().__init__()

    # This override is here because of my editor's OCD, but you can live without it
    @override
    def init(self, screen: pygame.Surface):
        pass

    @override
    def render(self, screen: pygame.Surface):
        # screen.blit(self.rect, pygame.Rect(20, 20, 50, 50))
        screen.fill((255, 255, 255))
        self.board.draw(screen)
        self.tetromine.draw(screen)

    @override
    def update(
        self, events: list[pygame.Event], manager: GameManager, screen: pygame.Surface
    ):
        pass

    @override
    def stop(self):
        pass
