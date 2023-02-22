from src.globals import Globals
from typing import Callable
from src import sort
import pygame


DEVAGAR = 30
QUASE_PARANDO = 1
RAPIDO = 1200
MAIS_OU_MENOS = 600



class RunSortMethod:

    def __init__(self, method: Callable, frame_rate: int) -> None:
        self.method = method
        self.frame_rate = frame_rate
    
    def start(self) -> None:
        self.method(Globals.array)
        Globals.is_running = False
    
    @staticmethod
    def get_sort_method() -> 'RunSortMethod':
        method, frame_rate = {
            "quick_sort": (sort.quick_sort, DEVAGAR),
            "merge_sort": (sort.merge_sort, QUASE_PARANDO),
            "bubble_sort": (sort.bubble_sort, RAPIDO),
            "selection_sort": (sort.selection_sort, DEVAGAR),
            "insertion_sort": (sort.insertion_sort, DEVAGAR),
            "heap_sort": (sort.heap_sort, DEVAGAR),
            "counting_sort": (sort.counting_sort, DEVAGAR),
            "radix_sort": (sort.shell_sort, MAIS_OU_MENOS),
            "bucket_sort": (sort.cocktail_sort, RAPIDO)
        }.get(Globals.sort_method_name)
        return RunSortMethod(method, frame_rate)
    
    @staticmethod
    def run() -> None:
        sort_method = RunSortMethod.get_sort_method()
        Globals.frame_rate = sort_method.frame_rate
        Globals.thread = pygame.threads.Thread(target = sort_method.start) 
        Globals.thread.start()
