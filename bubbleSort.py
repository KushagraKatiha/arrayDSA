## Bubble Sort

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                # arr[j], arr[j+1] = arr[j+1], arr[j]

                            # OR 

                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp 
    return arr        

arr = [70, 20, 50, 30, 90, 5, 15]

bSortResult = bubbleSort(arr)
print("After applying bubble  =>",bSortResult)