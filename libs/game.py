# type:ignore[reportImportCycles]
# Ignore the circular import error
from abc import ABC, abstractmethod
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libs.game_manager import GameManager

class Game(ABC):
    """
    This is the Game's Base Class. All Games will inherit from this class, and you must override the methods, otherwise an error will be thrown
    """
    @abstractmethod
    def init(self, screen: pygame.Surface):
        """
        Initialize your game's variables here, for example loading colors and all will fall here
        """
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        """
        Render stuff to the screen, for example, all the `blits` go here, 
        this is optional? just write an empty function in case you plan to do everything inside the update loop.

        This will be repeated 60 times per second inside the game
        """
        pass

    @abstractmethod
    def update(self, events: list[pygame.Event], manager: 'GameManager', screen: pygame.Surface):
        """
        Update Stuff Here, for example all the calculations and movements go here that you need to change every frame.
        Ideally this method should contain just that, but I won't hold it against ya if you also render stuff here.

        This too shall be repeated 60 times per second.
        """
        pass

    # TODO: check if this is being called.
    @abstractmethod
    def stop(self):
        """
        Cleanup stuff here.
        """
        pass

