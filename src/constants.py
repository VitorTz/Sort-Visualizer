from src.colors import Colors
from pygame import K_SPACE, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9
from pathlib import Path


class Constants:

    # window
    window_width = 1280
    window_height = 720
    window_size = (window_width, window_height)
    window_bg_color = Colors.grey
    window_title = "Sort Visualizer"

    # array bar
    bar_color = Colors.blue
    bar_width = 1

    # array
    array_size = window_width // bar_width

    # keyboard
    reset_key = K_SPACE
    digit_keys = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
    digits: dict[int, int] = {
        x+1: i for i, x in enumerate(digit_keys)
    }

    # font
    font = Path("res/SourceCodePro-Semibold.otf")
    font_size = 16
    font_color = Colors.white

    # menu imgs
    menu_img_by_sort_method: dict[str, Path] = {
        "merge_sort": Path("res/menu/menu_merge.png"),
        "quick_sort": Path("res/menu/menu_quick.png"),
        "bubble_sort": Path("res/menu/menu_bubble.png"),
        "selection_sort": Path("res/menu/menu_selection.png"),
        "insertion_sort": Path("res/menu/menu_insertion.png"),
        "heap_sort": Path("res/menu/menu_heap.png"),
        "counting_srt": Path("res/menu/menu_counting.png"),
        "radix_sort": Path("res/menu/menu_radix.png"),
        "bucket_sort": Path("res/menu/menu_bucket.png")
    }

    method_name_by_number: dict[int, str] = { 
        1: "merge_sort",
        2: "quick_sort",
        3: "bubble_sort",
        4: "selection_sort",
        5: "insertion_sort",
        6: "heap_sort",
        7: "counting_sort",
        8: "radix_sort",
        9: "bucket_sort"
    }

    menu_pos = (20, 20)
