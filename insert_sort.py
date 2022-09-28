#python3


def insert_sort(arr: list[int]):
    """
    Insert Sort
    
    """
    
    for i in range(1, len(arr)):
        value = arr[i]
        
        pos = i - 1
        for j in range(i-1, -1, -1):
            if arr[j] > value:
                arr[j+1] = arr[j]
            else:
                pos = j
                break
        
        arr[pos+1] = value
    
    return arr
