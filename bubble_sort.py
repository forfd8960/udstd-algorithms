
""" Bubble Sort
1. Bubble Up the largest element to the last position.
2. Repeat step1, bubble up the second largest element to index: n - 2
3. After n-1 passes(from 0 to n-2), the list is sorted

>>> from bubble_sort import bubble_sort
>>> bubble_sort([3, 2, 6, 1, 9])
i = 0, arr = [2, 3, 1, 6, 9]
i = 1, arr = [2, 1, 3, 6, 9]
i = 2, arr = [1, 2, 3, 6, 9]
i = 3, arr = [1, 2, 3, 6, 9]
[1, 2, 3, 6, 9]
"""

def bubble_sort(arr):
    last_idx = len(arr) - 1
    for i in range(0, last_idx):
        # after every bubble up, the num of elements need exchange decrease one
        for j in range(0, last_idx-i):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # bubble up large element to j+1
        print(f"i = {i}, arr = {arr}")
        
    return arr

"""
sort arr[3, 2, 6, 1, 9]

i = 0, arr[2, 3, 1, 6, 9]
i = 1, arr[2, 1, 3, 6, 9]
i = 2, arr[1, 2, 3, 6, 9]
i = 3, arr[1, 2, 3, 6, 9]
"""


