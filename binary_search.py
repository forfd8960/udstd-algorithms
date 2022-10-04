#python3

# https://time.geekbang.org/column/article/42520
def binary_search(arr, n, k):
    index = -1
    low, high = 0, n - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < k:
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            index = mid
            return index
        
    return index


def my_sqrt(n) -> float:
    if n <= 0:
        return 0.0
    
    low, high = 0, n
    mid = n / 2
    
    while abs(mid ** 2 - n) > 0.000001:
        if mid ** 2 < n:
            low = mid
        else:
            high = mid
            
        mid = (low + high) / 2

    return mid
