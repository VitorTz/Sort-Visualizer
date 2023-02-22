from src.globals import Globals, init_globals, reset_array, init_thread, kill_current_thread
from src.constants import Constants
from src.draw_array import draw_array
from src.sort_thread import SortThread
from src.menu import Menu
import pygame
import sys



def close() -> None:
    kill_current_thread()
    pygame.quit()
    sys.exit()


def reset_sort() -> None:
    kill_current_thread()
    reset_array()
    init_thread(SortThread(Globals.sort_name))


def change_sort_name(pressed_key: int) -> None:
    sort_name: str = Constants.sort_name_by_key[pressed_key]
    Globals.sort_name = sort_name


def handle_keyboard(pressed_key: int, menu: Menu) -> None:
    if pressed_key == Constants.pause_continue_key:
        reset_sort()
    elif pressed_key in Constants.sort_name_by_key.keys():
        change_sort_name(pressed_key)
        kill_current_thread()
        reset_sort()
        menu.update()
        

def check_events(menu: Menu) -> None:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            close()
        elif e.type == pygame.KEYDOWN:
            handle_keyboard(e.key, menu)


def main() -> None:

    init_globals()
    reset_sort()
    menu = Menu()
    while True:
        check_events(menu)
        Globals.display.fill(Constants.window_bg_color)
        draw_array()
        menu.main()
        pygame.display.update()


if __name__ == "__main__":
    main()