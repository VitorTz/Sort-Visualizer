from src.constants import Constants
from random import randint
import pygame



class Globals:

    is_running = True

    # late init
    display: pygame.Surface
    clock: pygame.time.Clock

    # array
    array: list[int]

    # sorting
    sorting_frame_rate: int = 0
    sort_name = "merge_sort"

    # thread (only one thread)
    thread: pygame.threads.Thread = None


def reset_array() -> None:
    Globals.array = [
        randint(1, Constants.window_height) for _ in range(Constants.window_width)
    ]

def init_globals() -> None:
    pygame.init()
    pygame.font.init()
    Globals.display = pygame.display.set_mode(Constants.window_size)
    Globals.clock = pygame.time.Clock()
    pygame.display.set_caption(Constants.window_title)
    reset_array()

def kill_current_thread() -> None:
    Globals.is_running = False
    if Globals.thread:
        Globals.thread.join()
    Globals.is_running = True

def init_thread(thread: pygame.threads.Thread) -> None:
    kill_current_thread()
    Globals.thread = thread
    Globals.thread.start()
