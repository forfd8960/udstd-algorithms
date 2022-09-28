#python3


def insert_sort(arr: list[int]):
    """
    Insert Sort
    
    """
    
    for i in range(1, len(arr)):
        value = arr[i]
        
        pos = i - 1
        while pos >= 0:
            if arr[pos] > value:
                arr[pos+1] = arr[pos]
                print(f"   j = {pos}, value = {value}, arr = {arr}")
                pos -= 1
            else:
                break
        arr[pos+1] = value
        print(f"i = {i}, arr: {arr}")

    return arr
