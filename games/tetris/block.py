from copyreg import constructor
from enum import Enum
from pprint import pprint
import random
from typing import override
import pygame


class Block(object):
    block_size: int
    x: int
    y: int
    rect: pygame.Rect

    def __init__(self, block_size: int, start_pos: tuple[int, int]):
        self.block_size = block_size
        self.x = (int(800 / 2) - int(10 / 2) * block_size) + start_pos[0] * block_size
        self.y = (int(800 / 2) - int(20 / 2) * block_size) + start_pos[1] * block_size

        self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)


class TetroMine(Enum):
    I = [[1, 1, 1, 1]]
    O = [[1, 1], [1, 1]]
    T = [[1, 1, 1], [0, 1, 0]]
    S = [[0, 1, 1], [1, 1, 0]]
    Z = [[1, 1, 0], [0, 1, 1]]
    J = [
        [1, 0, 0],
        [1, 1, 1],
    ]
    L = [
        [0, 0, 1],
        [1, 1, 1],
    ]

    @override
    def __repr__(self) -> str:
        # return f"{self.value}"
        cls = self.__class__
        return f"{cls.__name__}\n" + "\n".join(
            ["".join(["#" if i else " " for i in j]) for j in self.value]
        )

    @classmethod
    def random(cls):
        # return TetroMine.I
        return random.choice(list(cls))

    def __init__(self, val: list[list[int]]) -> None:
        self.start_pos_y = random.randrange(0, 9 - len(val[0]) - 1)
        self.start_pos_y = 0
        self.blocks: list[Block] = []

        for j_index, j in enumerate(val):
            for i_index, i in enumerate(j):
                if i:
                    block = Block(30, (self.start_pos_y + i_index, j_index))
                    self.blocks.append(block)

    def draw(self, screen: pygame.Surface):
        for block in self.blocks:
            block.draw(screen)
