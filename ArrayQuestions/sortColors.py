arr = [2, 0, 2, 1, 1, 0]

def sortColor(arr):
    x = len(arr)
    curr = 0
    pointer_1 = 0 
    pointer_2 = x-1

    while curr <= pointer_2:
        if arr[curr] == 0:
            arr[curr], arr[pointer_1] = arr[pointer_1], arr[curr]
            pointer_1 += 1
            curr += 1
        elif arr[curr] == 2:
            arr[curr], arr[pointer_2] = arr[pointer_2], arr[curr]
            pointer_2 -= 1
        else:
            curr += 1

    return arr

result = sortColor(arr) 
print(result)