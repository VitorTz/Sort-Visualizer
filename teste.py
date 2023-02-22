
def merge_sort(array: list):
    curr_size = 1
    n = len(array)
    
    while curr_size < n - 1:
        left = 0
        while left < n - 1:
            mid = min((left + curr_size - 1), (n-1))
            right = ((2 * curr_size + left - 1, n - 1)[2 * curr_size + left - 1 > n-1])
            merge(array, left, mid, right)
            left = left + curr_size * 2
        curr_size = 2 * curr_size

def merge(array: list, left: int, mid: int, right: int):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[left + i]

    for i in range(0, n2):
        R[i] = array[mid + i + 1]

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if L[i] > R[j]:
            array[k] = R[j]
            j += 1
        else:
            array[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
