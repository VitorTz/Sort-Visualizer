from src.globals import Globals
from src.constants import Constants
import pygame




def draw_array() -> None:
    for i, height in enumerate(Globals.array):
        pygame.draw.rect(
            Globals.display,
            Constants.bar_color,
            (
                i, 
                Constants.window_height - height,
                Constants.bar_width,
                height
            )
        )