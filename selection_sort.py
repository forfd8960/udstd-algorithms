# python3

def selection_sort(arr):
    i = 0
    last_idx = len(arr) - 1
    
    for i in range (0, last_idx):
        min = i
        
        for j in range (i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
        
        print(f"i = {i}, arr = {arr}")
    
    return arr

## sort arr[3, 2, 6, 1, 9]

## i = 0, min = 3, arr[1, 2, 6, 3, 9]
## i = 1, min = 1, arr[1, 2, 6, 3, 9]
## i = 2, min = 3, arr[1, 2, 3, 6, 9]
## i = 3, min = 3, arr[1, 2, 3, 6, 9]