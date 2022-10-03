
def count_sort(arr: list[int]) -> list[int]:
    """
    In [1]: from count_sort import count_sort
    In [2]: arr = [22, 5, 11, 41, 45, 26, 29, 10, 7, 8, 30]
    In [3]: sorted_arr = count_sort(arr)
    In [4]: sorted_arr
    Out[4]: [5, 7, 8, 10, 11, 22, 26, 29, 30, 41, 45]
    """
    if len(arr) <= 1:
        return arr

    max_v = max(arr)
    count_arr = [0 for _ in range(0, max_v+1)]
    for x in arr:
        count_arr[x] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i-1] + count_arr[i]

    result = [None for _ in range(0, len(arr))]
    for x in range(len(arr)-1, -1, -1):
        idx = count_arr[arr[x]] - 1
        result[idx] = arr[x]
        count_arr[arr[x]] -= 1

    return result
