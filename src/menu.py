from src.constants import Constants
from src.globals import Globals
from pathlib import Path
from src.image import Image



class Menu:

    def __init__(self) -> None:
        self.__image = Image(self.menu_img, Constants.menu_pos)
    
    @property
    def menu_img(self) -> Path:
        return Constants.menu_img_by_sort_method.get(
            Globals.sort_method_name
        )
    
    def change_img(self) -> None:
        self.__image.image = self.menu_img
    
    def main(self) -> None:
        self.__image.draw()