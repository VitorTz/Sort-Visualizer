from src.globals import Globals
from pathlib import Path
import pygame


class Image:

    def __init__(self, image: Path, left_top_pos: tuple[int, int]) -> None:
        self.image = image
        self.rect = left_top_pos
    
    @property
    def image(self) -> pygame.Surface:
        return self.__image

    @image.setter
    def image(self, image: Path):
        if isinstance(image, Path):
            self.__image = pygame.image.load(image)
        elif isinstance(image, str):
            self.image = Path(image)
    
    @property
    def rect(self) -> pygame.Rect:
        return self.__rect

    @rect.setter
    def rect(self, pos: tuple[int, int]):
        self.__rect = self.image.get_rect()
        self.__rect.left, self.__rect.top = pos
    
    def draw(self) -> None:
        Globals.display.blit(self.image, self.rect)