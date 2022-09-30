# python3


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    return quic_sort(arr, 0, len(arr)-1)


def quic_sort(arr, low, high):
    if low >= high:
        return arr

    pivot = partition(arr, low, high)
    quic_sort(arr, 0, pivot-1)
    quic_sort(arr, pivot+1, high)

    return arr


def partition(arr: list[int], low, high) -> int:
    if len(arr) <= 1:
        return 0
    
    pivot = arr[low]
    
    i, j = low+1, high
    while True:
        while i <= high:
            if arr[i] < pivot:
                i += 1
            else:
                break
            
        if i >= j:
            break

        while j > 0:
            if arr[j] > pivot:
                j -= 1
            else:
                break
            
        if i >= j:
            break

        if i != j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1

# find kth large element in the arr
def find_kth_element(arr: list[int], k: int) -> int:
    if k > len(arr) or k <= 0:
        return -1

    xk = len(arr) - (k - 1) - 1
    return find_kth_in_arr(arr, xk, 0, len(arr)-1)


def find_kth_in_arr(arr: list[int], k, low, high) ->  int:
    pivot = partition(arr, low, high)
    if k < pivot:
        return find_kth_in_arr(arr, k, low, pivot-1)
    
    if k > pivot:
        return find_kth_in_arr(arr, k, pivot+1, high)
    
    return arr[pivot]
