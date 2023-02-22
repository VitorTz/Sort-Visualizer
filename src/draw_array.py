from src.constants import Constants
from src.globals import Globals
import pygame



def draw_bar(index: int, height: int) -> None:
    rect = pygame.Rect(index, 0, 1, height)
    rect.bottom = Constants.window_height
    pygame.draw.rect(
        Globals.display,
        Constants.bar_color,
        rect
    )


def draw(array: list[int]) -> None:
    for index, height in enumerate(array):
        draw_bar(index, height)