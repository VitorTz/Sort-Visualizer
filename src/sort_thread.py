from src.globals import Globals
from typing import Callable
from src import sort
import pygame


class SortMethod:


    def __init__(self, method: Callable, frame_rate: int) -> None:
        self.method = method
        self.frame_rate = frame_rate


def get_sort_method_by_name(name: str) -> SortMethod:
    slowwwwwww = 1
    slow = 30
    medium = 600
    fast = 1200

    method, frame_rate =  {
        "quick_sort": (sort.quick_sort, slow),
        "merge_sort": (sort.merge_sort, slowwwwwww),
        "bubble_sort": (sort.bubble_sort, fast),
        "selection_sort": (sort.selection_sort, slow),
        "insertion_sort": (sort.insertion_sort, fast),
        "heap_sort": (sort.heap_sort, slow),
        "counting_sort": (sort.counting_sort, slow),
        "shell_sort": (sort.shell_sort, medium),
        "cocktail_sort": (sort.cocktail_sort, fast),
    }.get(name)
    return SortMethod(method, frame_rate)


class SortThread(pygame.threads.Thread):

    def __init__(self, sort_name: str) -> None:
        self.__sort_method: SortMethod = get_sort_method_by_name(sort_name)
        Globals.sorting_frame_rate = self.__sort_method.frame_rate
        super().__init__(
            target= lambda : self.__sort_method.method(Globals.array)
        )
    

