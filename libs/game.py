from abc import ABC, abstractmethod
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from libs.game_manager import GameManager

class Game(ABC):
    @abstractmethod
    def init(self):
        """
        Init stuff here
        """
        pass

    @abstractmethod
    def render(self, screen: pygame.Surface):
        """
        Render Stuff Here
        """
        pass

    @abstractmethod
    def update(self, events: list[pygame.Event], manager: 'GameManager', screen: pygame.Surface):
        """
        Update Stuff Here
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Cleanup stuff here
        """
        pass

