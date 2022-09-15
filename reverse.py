
def reverse(arr):
    i = 0
    j = len(arr) - 1
    while i != j and i < len(arr) // 2:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
        
    return arr

def reverse_group(arr, k):
    n = len(arr) // k
    print(f"n = {n}")
    for i in range(0, n):
        start = i * k
        arr = reverse1(arr, start, start + k - 1)
        print(f"start = {start}, arr = {arr}")

    return arr


def reverse1(arr, low, high):
    if low == high:
        return arr
    
    i = low
    j = high
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
        j = j - 1
        
    return arr