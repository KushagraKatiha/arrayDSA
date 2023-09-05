## Search for the given target in the 2D-array and if it is present in the array return True else False

# Array
arr = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]

# Target
target = 7

####################### Brute Force Approach #############################

def linearSearchIn2D(arr, target):
    # No. of rows 
    r = len(arr)

    # No. of columns
    c = len(arr[0])
    for i in range (r):
        for j in range(c):
            if arr[i][j] == target:
                return True
    return False

## Function Call
result = linearSearchIn2D(arr, target)
print(result)


############################# Binary Search Approach ###############################

def binarySearchIn2D(arr, target):
    # No. of rows 
    r = len(arr)

    # No. of columns
    c = len(arr[0])
    # low & high of matrix
    low , high = 0, (r*c)-1
    if r == 0:
        return False
    else:
        while low<=high:
            # mid of the matrix
            mid = low + (high - low) // 2

            # mid element => arr[mid//c][mid%c]

            if arr[mid//c][mid%c] == target:
                return True
            elif arr[mid//c][mid%c] > target:
                high = mid-1
            else: 
                low = mid+1
        
    return False

## Function call 
result2 = binarySearchIn2D(arr, target)
print(result2)
    
                 
