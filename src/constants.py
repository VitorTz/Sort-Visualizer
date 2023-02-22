from src.colors import Colors
from pathlib import Path
import pygame



class Constants:


    # window
    window_width = 1280
    window_height = 720
    window_size = (window_width, window_height)
    window_title = "Sort Visualizer"
    window_bg_color = Colors.grey

    # bar
    bar_color = Colors.blue
    bar_width = 1

    # keys
    reset_key: int = pygame.K_r
    pause_continue_key: int = pygame.K_SPACE
    sort_name_by_key: dict[int, str] = {
        pygame.K_1: "merge_sort",
        pygame.K_2: "quick_sort",
        pygame.K_3: "bubble_sort",
        pygame.K_4: "selection_sort",
        pygame.K_5: "insertion_sort",
        pygame.K_6: "counting_sort",
        pygame.K_7: "heap_sort",
        pygame.K_8: "shell_sort",
        pygame.K_9: "cocktail_sort"
    }

    menu_img_by_sort_name: dict[str, Path] = {
        "merge_sort": Path("res/menu/merge_sort.png"),
        "quick_sort": Path("res/menu/quick_sort.png"),
        "bubble_sort": Path("res/menu/bubble_sort.png"),
        "selection_sort": Path("res/menu/selection_sort.png"),
        "insertion_sort": Path("res/menu/insertion_sort.png"),
        "heap_sort": Path("res/menu/heap_sort.png"),
        "counting_sort": Path("res/menu/counting_sort.png"),
        "shell_sort": Path("res/menu/shell_sort.png"),
        "cocktail_sort": Path("res/menu/cocktail_sort.png")
    }

    menu_img_pos = [10, 10]
