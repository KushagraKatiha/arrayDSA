## Insertion Sort

def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key

    return arr        


## Driver Code
arr = [9, 5, 1, 4, 3]

result = insertionSort(arr)
print(result)