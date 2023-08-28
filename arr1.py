arr=[2,1,8,9,12,15,11,19]

# Search for an lement "15" and if it's present in an array, return the index of that element
# Suppose the searchig element is not present in an array, return -1
### Time Complexity : O(n)
### Space Complexity : O(1)
## Function Defination

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1    


# Driver code
x = 20
# function calling

result = linearSearch(arr,x)
print("Searching element is present at the index", result)




## Insert an element 5 at index 2
## Time Complexity : O(n)

arr.insert(2, 5)

print(arr)

## Remove an element 8 from the array 
## Time Complexity : O(n)
arr.remove(8)
print(arr)

## Counting the occurance of given element
print(arr.count(11))

## Delete an element providing the index
arr.pop(0)
print(arr)

## Sort the array
arr.sort()
print(arr)

## Getting the index of given element
print(arr.index(11))

## To extent the original array 
arr.extend([0,1,2,3,4])
print(arr)

## Reverse the entire array
arr.reverse()
print(arr)