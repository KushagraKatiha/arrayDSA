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



