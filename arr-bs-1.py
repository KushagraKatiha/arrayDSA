# Problem Statement:- We have an array we have certain integers and after them all the values are infinite "inf", we have to find the index of very first "inf" character

# Solution:- 
arr = [1,5,8,9,6,-50,-8,float('inf'),float('inf'),float('inf'),float('inf'),float('inf')]

## Using linear search

def linear(arr, x):
    for i in range (len(arr)):
        if arr[i] == x:
            return i
    
result = linear(arr, float('inf'))
print(result)

## Using binary search

def binary(arr, i, j, x):
    while i<=j:
        mid = i + (j-i) // 2
        if arr[mid] != x:
            return binary(arr, mid+1, j, x)
        else:
            if arr[mid-1] != x:
                return mid
            else:
                return binary(arr,i,mid-1,x)
        
i = 0
j = len(arr)-1
x = float('inf')

result2 = binary(arr,i,j,x)
print(result2)