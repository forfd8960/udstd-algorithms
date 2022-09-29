# python3


def merge_sort(arr: list[int]) -> list[int]:
    """
    In [1]: from merge_sort import merge_sort
    In [2]: arr = merge_sort([1,3,2,5,6])

    In [3]: arr
    Out[3]: [1, 2, 3, 5, 6]

    In [4]: arr = merge_sort([1])

    In [5]: arr
    Out[5]: [1]

    In [6]: arr = merge_sort([9,3])

    In [7]: arr
    Out[7]: [3, 9]

    In [8]: arr = merge_sort([9,3,7])

    In [9]: arr
    Out[9]: [3, 7, 9]
    """
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:len(arr)]

    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)
    return merge_arr(arr1, arr2)


def merge_arr(arr1, arr2) -> list[int]:
    new_arr = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
            
    for idx in range(i, len(arr1)):
            new_arr.append(arr1[idx])
        
    for idx in range(j, len(arr2)):
            new_arr.append(arr2[idx])

    return new_arr
