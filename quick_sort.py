# python3


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    return quic_sort(arr, 0, len(arr)-1)


def quic_sort(arr, low, high):
    if low >= high:
        return arr

    pivot = partion(arr, low, high)
    quic_sort(arr, 0, pivot-1)
    quic_sort(arr, pivot+1, high)

    return arr


def partion(arr: list[int], low, high) -> int:
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
