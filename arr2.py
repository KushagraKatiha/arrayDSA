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
    return -1  

## Ternary Search

def ternarySearch(arr, x, lb, ub):
    while lb<=ub:
        mid1 = lb + (ub-lb) // 3       
        mid2 = ub - (ub-lb) // 3

        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif arr[mid1] > x:
            ub = mid1-1
        elif arr[mid2] < x:
            lb = mid2+1
        else:
            ub = mid2-1
            lb = mid1+1

    return -1            


arr = [1,2,3,4,5,6,8]
                                   
lb = 0
ub = len(arr)-1
x = 4

linearResult = linearSearch(arr, x)
binaryResult = binarySearch(arr, lb, ub, x)
ternaryResult = ternarySearch(arr, x, lb, ub)

print(linearResult)
print(binaryResult)
print(ternaryResult)