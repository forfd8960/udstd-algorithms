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


# Find the first idx for given value when there are repeated values in arr
def binary_search_first_value(arr, value) -> int:
    index = -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != value:
                return mid

            high = mid - 1

    return index


# find last idx for a given value
def binary_search_last_value(arr, value) -> int:
    index = -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] != value:
                return mid
            
            low = mid + 1

    return index


# Find the first index, which arr[index] >= value
def binary_search_first_gte_value(arr, value) -> int:
    index = -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] >= value:
            if mid == 0 or arr[mid - 1] < value:
                return mid
            high = mid - 1
        else:
            low = mid + 1
        

    return index


# FInd the last index, which arr[index] <= value
def binary_search_last_lte_value(arr, value) -> int:
    index = -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if arr[mid] <= value:
            low = mid + 1
        else:
            high = mid - 1

    return index
