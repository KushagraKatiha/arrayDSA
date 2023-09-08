## Selection Sort
def selectionSrt(arr):
    x = len(arr)
    for i in range(x):
        min = i
        for j in range((i+1), x):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


## Driver Code

arr = [50, 38, 45, 79, 19, 27, 29]

result = selectionSrt(arr)
print(result)