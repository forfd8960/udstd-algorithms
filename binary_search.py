#python3


def binary_search(arr, n, k):
    index = -1
    left, right = 0, n - 1
    while right >= left:
        mid = (left + right) // 2
        if arr[mid] < k:
            left = mid + 1
        elif arr[mid] > k:
            right = mid - 1
        else:
            index = mid
            return index
        
    return index
