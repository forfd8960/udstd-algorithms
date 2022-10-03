#python3

from quick_sort import quick_sort


def bucket_sort(arr: list[int]) -> list[int]:
    """
    In [1]: from bucket_sort import bucket_sort
    In [2]: arr = [22, 5, 11, 41, 45, 26, 29, 10, 7, 8, 30]

    In [3]: sorted_arr = bucket_sort(arr)

    In [4]: sorted_arr
    Out[4]: [5, 7, 8, 10, 11, 22, 26, 29, 30, 41, 45]
    """
    if len(arr) <= 1:
        return arr
    
    max_v = max(arr)
    num_bucket = max_v // 10
    if max_v % 10 > 0:
        num_bucket += 1
    
    # init buckets
    buckets = [[] for _ in range(0, num_bucket)]
    # init value range in each bucket
    values_range = [(i*10, i*10+9) for i in range(0, num_bucket)]
    
    for x in arr:
        append_to_bucket(buckets, values_range, x)
    
    result = []
    for arr in buckets:
        sorted_arr = quick_sort(arr)
        result += sorted_arr

    return result


def append_to_bucket(buckets, values_range, x):
    for i, v_range in enumerate(values_range):
        if x <= v_range[1] and x >= v_range[0]:
            buckets[i].append(x)
            return
