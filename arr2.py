## Linear Search

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1 


## Binary Search 

def binarySearch(arr, lb, ub, x):
    while lb<=ub:
        mid = lb + (ub-lb) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, lb, mid-1, x)
        elif arr[mid] < x:
            return binarySearch(arr, mid+1, ub, x)




arr = [1,2,3,4,5,6,8]

lb = 0
ub = len(arr)-1
x = 5

linearResult = linearSearch(arr, x)
binaryResult = binarySearch(arr, lb, ub, x)

print(linearResult)
print(binaryResult)