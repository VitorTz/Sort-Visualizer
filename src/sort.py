from src.globals import Globals


def wait() -> None:
    Globals.clock.tick(Globals.sorting_frame_rate)


def quick_sort(arr: list[int]) -> None:
    stack = [(0, len(arr) - 1)]
    while stack and Globals.is_running:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[start]
        i, j = start + 1, end
        while i <= j:
            if arr[i] <= pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], pivot
        if j - start < end - j:
            stack.append((start, j - 1))
            stack.append((j + 1, end))
        else:
            stack.append((j + 1, end))
            stack.append((start, j - 1))
        wait()
    return arr


def merge_sort(arr):
    current_size = 1
    n = len(arr)
    
    while current_size < n - 1 and Globals.is_running:
        left = 0
        
        while left < n - 1:
            mid = min((left + current_size - 1), (n - 1))
            right = ((2 * current_size + left - 1, n - 1)[2 * current_size + left - 1 > n - 1])
            merge(arr, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size
        wait()

        
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(0, n1):
        L[i] = arr[l + i]
    for i in range(0, n2):
        R[i] = arr[m + i + 1]
        
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        if not Globals.is_running:
            break
        for j in range(0, n-i-1):
            if not Globals.is_running:
                break
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            wait()
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        if not Globals.is_running:
                break
        min_idx = i
        for j in range(i+1, n):
            if not Globals.is_running:
                break
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        wait()
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if not Globals.is_running:
            break
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            wait()
        arr[j+1] = key


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        if not Globals.is_running:
            break
        heapify(arr, n, i)
        wait()
        
    for i in range(n - 1, 0, -1):
        if not Globals.is_running:
            break
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        wait()
    return arr


def counting_sort(arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += 1
    i = 0
    for j in range(max_val + 1):
        if not Globals.is_running:
            break
        for k in range(counts[j]):
            if not Globals.is_running:
                break
            arr[i] = j
            i += 1
            wait()
    return arr


def shell_sort(arr):
    n = len(arr)
    h = 1

    # Determina o valor de h, seguindo a sequência de Ciura
    ciura_seq = [1750, 701, 301, 132, 57, 23, 10, 4, 1]
    for i in ciura_seq:
        if i < n:
            h = i
            break

    while h < n and Globals.is_running:
        # Realiza a ordenação para cada sublista de tamanho h
        for i in range(h, n):
            if not Globals.is_running:
                break
            temp = arr[i]
            j = i

            # Desloca os elementos da sublista em ordem crescente
            while j >= h and arr[j - h] > temp:
                arr[j] = arr[j - h]
                wait()
                j -= h

            arr[j] = temp

        # Reduz o valor de h para a próxima iteração
        h //= 2

    return arr



def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while swapped == True and Globals.is_running:
        swapped = False
        for i in range(start, end):
            if not Globals.is_running:
                break
            if (arr[i] > arr[i + 1]) :
                arr[i], arr[i + 1]= arr[i + 1], arr[i]
                wait()
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if not Globals.is_running:
                break
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                wait()
        start = start + 1
    return arr
