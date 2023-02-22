from src.constants import Constants
from random import randint
import pygame



class Globals:

    # Array a ser ordenado (late init)
    array: list[int]

    # display (late init)
    display: pygame.Surface
    clock: pygame.time.Clock

    # first method
    sort_method_name: str = "merge_sort"

    # late init
    thread: pygame.threads.Thread = None

    # window frame
    frame_rate = 0 # taxa de atualização do método de sort
    frame_count = 0 # contador de frames

    # status
    is_running = True


def reset_globals() -> None:
    Globals.array = [randint(1, Constants.window_height) for _ in range(Constants.array_size)]
    Globals.frame_count = 0
    Globals.is_running = True


def init_globals() -> None:
    pygame.init()
    pygame.font.init()
    Globals.display = pygame.display.set_mode(Constants.window_size)
    Globals.clock = pygame.time.Clock()
    pygame.display.set_caption(Constants.window_title)
    reset_globals()


