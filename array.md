# Array
Array is a linear data structure , means the data stored in array is in coninuous manner.

Let us say that we have an array that stores integers inside it so if the first integer is at position "100", the next integer will get the position of "104" (since the size of an integet is of 4 bit)

This property of array enable us to access any data inside the array randomly like if we want to access the last elemet we would not have to iterate over every element of the array same goes with the element present at the middle or at any position inside an array 

## Indexing of an array
The indexing of an array in many of languages like C, C#, C++, JavaScript, Python, Java etc. starts with zero. <br> 

So if any array has the maximum index of 5 it is easy to understand that the total number of elements present in it will be 6 as:-

### "first element will have index as 0" , "second element will have index as 1" , "third element will have index as 2" , "fourth element will have index as 3" , "fifth element will have index as 4" and "sixth element will have index as 5" 

### Defining an array:- 
`
arr = [1,5,4,8,6,3]  
`

### Accessing random element:- 

`
arr[0]      // output 1  
`

`
arr[3]      //output 8
`

`
To access last element of an array:-  arr[n-1]    (where n = total number of elements in an array)
`

## Accessing Memory address of an array

Suppose we have an array as `arr = [1,2,3,4,5,6]` and memory address of the element of very first index is 1000 i.e. `address of arr[0] is 1000` so the address of the random element in the array will be `base address + (i - lower bound of and index) * size of element`  
`
where i = index of the element whose address is required, 
`   
So in our case if we want to calculate the address of "3" 
`
address of 3 => 1000 + (2-0) * 4 = "1008"
`

# The 2D Array 

There exists the concept of 2D array or we can say "Two Dimensional Array" and they can be seen as :- 

1 2 3  
4 5 6  
7 8 9

but in the memory there is no such concept of two dimensions in the memory the 2D array will be stored as that of 1D array ( normal array ) only. 
 
`ex:- 1 2 3 4 5 6 7 8 9`

and to access the memory address of any of the element we use the same method that we use in the normal array.

## Accessing the element of 2D array

To access any element of the 2D array we can use the concept of two indices, we can imagine the array as :-

<pre>

   [j] 1 2 3  
[i]   
 1     0 5 6    
 2     7 8 9  
 3     7 9 6
</pre>

j be the index of the column and i be the index of row and to access any specific element of the 2D matrix we use the syntax written below

`arr[i][j]`  
ex:- To access 0 from the above matrix we can write:-   
`arr[1][1]`

# Linear Search 
Linear search means to search a given element in the array linearly , suppose we have an array :-  
`arr = [1,5,6,2,8,9]`  
and we have to search for the element "6" in the array, now if the element is present in array linear search algorithm will provide the index of that element and if not it will provide "-1" which will indicate that the element is not present in the array.   

<pre>
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
</pre>  

the above function defines the linear search now, if we want to search for "6" we will call the function will respective parameters

<pre>
   x = 6
   result = linearSearch(arr, x)
   print("Element is present at index:- ", result)

   // output:- Element is present at index 2
</pre>

## Time complexity 
The time complexity of the linear search is O(n) as we are using only single for loop and in the worst case it will traverse the whole array. 

# Binary Search 
In binary search we the divide and conqure approach in order to search for the given element. 
We divide the array into two sub-arrays from the middle of the array.  

**Binary search is used on the array which is already sorted  

### The below example will help you uderstand the full concept of the binary search

Suppose we have an array:-   
`arr = [2,5,6,9,11,45,100,205,300]` 

### Problem Statement:- 
In the given array we have to find if the element "x=205 is present in the array, if yes print the index of the element else print "-1".  
(Note:- Solve the problem using binary search only)
### Solution:-   
To use binary search:-   
Step 1 => Check if the array is sorted or not.  
Step 2 => Find the index of the middle element  
<pre>
    suppose i be the lower index,
    suppose j be the upper index i.e. len(arr)-1
    therefore, mid = i + (j-i)//2 (will provide the mid index)

    i = 0
    j = 8
    mid = 4
</pre>

`Note:- we do not use i+j // 2 in order to find the mid index as it can cause the problem of overflow if the values of i and j are too large`

Step 3 => Compare the element with the "arr[mid]", 
<pre>
    if "arr[mid] == x" return mid
    elif "arr[mid] > x", apply binary search in left sub-array, now (j=mid-1)
    else apply binary search in right sub-array, now (i=mid+1)
</pre>

Step 4 => Debugging the code 
<pre>
arr = [2,5,6,9,11,45,100,205,300]
x = 205
mid = 4
i = 0
j = 8

    arr[mid] = 11     // which is not equal to x
    arr[mid] < x      // now we have to search RSA

    right sub-array => [45,100,205,300]
      (i=mid+1)

i = 5
j = 8
mid = 6 

    again applying binary search
    arr[mid] = 100    // which is not equal to x
    arr[mid] < x      //now we have to search RSA

    right sub-array => [205,300]
      (i=mid+1)

i = 7
j = 8
mid = 7

    again applying binary search
    arr[mid] = 205    // which is equal to x
    return mid i.e. 
</pre>

This example must have helped you understanding the concept of binary search, try finding some other element with the same steps.

## Coding Implementation
### Coding implementaion using recursion

<pre>
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

binaryResult = binarySearch(arr, lb, ub, x)

print(binaryResult)
</pre>


### Coding implementaion without using recursion

<pre>
  def binarySearch(arr, lb, ub, x):
    while lb<=ub:
        mid = lb + (ub-lb) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            ub = mid - 1
        elif arr[mid] < x:
            lb = mid + 1

arr = [1,2,3,4,5,6,8]
lb = 0
ub = len(arr)-1
x = 5

binaryResult = binarySearch(arr, lb, ub, x)

print(binaryResult)
</pre>