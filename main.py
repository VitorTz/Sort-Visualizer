from src.globals import Globals, init_globals, reset_globals
from src.run_sort_method import RunSortMethod
from src.constants import Constants
from src.menu import Menu
from src import draw_array
import pygame
import sys



def stop_sort() -> None:
    Globals.is_running = False
    if Globals.thread:
        Globals.thread.join()


def start_sort() -> None:
    Globals.is_running = True
    RunSortMethod.run()


def reset_sort() -> None:
    stop_sort()
    start_sort()

def reset() -> None:
    reset_globals()
    reset_sort()


def change_sort_method(method_name: str, menu: Menu) -> None:
    if method_name != Globals.sort_method_name:
        Globals.sort_method_name = method_name
        reset()
        menu.change_img()   


def check_events(menu: Menu) -> None:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            stop_sort()
            pygame.QUIT
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == Constants.reset_key:
                reset()
            if e.key in Constants.digit_keys:
                digit_pressed: int = Constants.digits[e.key]
                change_sort_method(
                    Constants.method_name_by_number[digit_pressed],
                    menu
                )
                


def main() -> None:
    init_globals()
    start_sort()
    menu = Menu()
    while True:
        check_events(menu)
        Globals.display.fill(Constants.window_bg_color)
        draw_array.draw(Globals.array)
        menu.main()
        pygame.display.update()
    

if __name__ == "__main__":
    main()
        