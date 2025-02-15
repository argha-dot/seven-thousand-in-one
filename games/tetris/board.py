import pygame


class Board(object):
    grid_item_size: int
    hor_items: int
    vert_items: int
    start_point: tuple[int, int]

    def __init__(self, grid_item_size: int, vert_items: int, hor_items: int) -> None:
        self.grid_item_size = grid_item_size
        self.vert_items = vert_items
        self.hor_items = hor_items
        self.start_point = (
            int(800 / 2) - int(self.vert_items / 2) * self.grid_item_size,
            int(800 / 2) - int(self.hor_items / 2) * self.grid_item_size,
        )

    def draw(self, screen: pygame.Surface):
        for i in range(0, self.hor_items + 1):
            pygame.draw.line(
                screen,
                (255, 0, 0),
                (self.start_point[0], self.start_point[1] + i * self.grid_item_size),
                (
                    self.start_point[0] + self.vert_items * self.grid_item_size,
                    self.start_point[1] + i * self.grid_item_size,
                ),
            )

        for j in range(0, self.vert_items + 1):
            pygame.draw.line(
                screen,
                (255, 0, 0),
                (self.start_point[0] + j * self.grid_item_size, self.start_point[1]),
                (
                    self.start_point[0] + j * self.grid_item_size,
                    self.start_point[1] + self.hor_items * self.grid_item_size,
                ),
            )
