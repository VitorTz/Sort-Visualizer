from src.constants import Constants
from src.globals import Globals
from pathlib import Path
import pygame


class Image:

    def __init__(self, image: Path, pos: tuple[int, int]) -> None:
        self.__image = pygame.image.load(image)
        self.__rect = self.__image.get_rect()
        self.__rect.left, self.__rect.top = pos
    
    def change_img(self, image: Path) -> None:
        self.__image = pygame.image.load(image)
    
    def draw(self) -> None:
        Globals.display.blit(self.__image, self.__rect)


class Menu:

    def __init__(self) -> None:
        self.__image = Image(self.menu_img, Constants.menu_img_pos)
    
    @property
    def menu_img(self) -> Path:
        return Constants.menu_img_by_sort_name.get(Globals.sort_name)

    def update(self) -> None:
        self.__image.change_img(self.menu_img)

    def main(self) -> None:
        self.__image.draw()