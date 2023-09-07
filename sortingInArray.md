# Sorting In An Array

Sorting an array means to arrange the array in either increasing or in decreasing order, suppose we have an array :  
`arr = [20, 50, 11, 30, 5, -17, -100, 100, 64, 10]`  

The sorted array will look like :   

`arr = [-100, -17, 5, 10, 11, 20, 30, 50, 64, 100]` 
(Increasing Order)   
or  
`arr = [100, 64, 50, 30, 20, 11, 10, 5, -17, -100]`
(Decreasing Order)  

Now there are different methods to sort an array we will now discuss about them

## Methods to Sort an Array

There are two main methods to sort an array : 

<pre>
1 - Comparison Based Sorting
2 - Non-Comparison Based 
</pre>

### Comparison Based Sorting 

As the name suggests this sorting method is based on the comparision of the elements of the array, there are many methods which lies under this, main of them are :  
<pre>
Selection Sort
Bubble Sort
Insertion Sort
Quick Sort
Merge Sort
Heap Sort
</pre>

These methods are used to sort an array, now you might think if by using any of the method we can sort the array so why are there different methods ??  

Here is the answer, these all methods have different approaches to sort an array which have different time and space complexities and in different scenarios we use different methods accordingly.

Here The "Quick Sort" and "Merge Sort" are the applications of the divide and conqure technique

## Non-Comparison Based Sorting

As the name suggests this type of sorting don't use comparison of array elements they have completely differet approach to sort an array, some main non-comparison based sorting methods are :  

<pre>
Count Sort
Radix Sort
Bucket Sort
</pre>

## Stable vs Unstable Sorting

While moving further these are some key points that we have to keep in mind, here we will discuss about stable vs unstable sorting.   

<pre>
Explaing the stable and unstable sorting might be quite complicated so here I'll be using an example to illustrate that what does stable and unstable sorting actually means  

    Suppose we have an array=> arr = [1,5,6(a),8,4,2,6(b)] 

Here we can se we have two 6(s), for our convenience I have marked the first 6 as 6(a) and second 6 as 6(b)
</pre>

Now if use any sorting method and we get the final sorted array as:  

`arr = [1, 2, 4, 5, 6(b), 6(a), 8]`  

What do you think which type of sorting is this ??  

I think everyone have guessed it right the original order of both the 6(s) have changed and it makes the sorted array unstable and it is the only difference between stable and unstable sorting. (try to make stable sorted array from the above example.)

After this discussion we can say that:   
<pre>
In "Stable Array" the original order of the elements (if more than one element of same vale exists) do not get changed after sorting while in "Unstable Array" the original order of the elements get changes after sorting the array.
</pre>

I hope from the above example you have understood, what stable and unstable sorting is and what's the major difference between them. 

## Inplace vs Outplace Sorting

We can understand both the terms with their defination which says that =>  

<pre>
Inplace Sorting Algorithm :
     An in-place algorithm is an algorithm that does not need an extra space and produces an output in the same memory that contains the data by transforming the input ‘in-place’. However, a small constant extra space used for variables is allowed.
</pre>

So in-place sorting does not need any extra space in the memory and sort the array within the memory which is allocated to the original array

<pre>
Outplace Sorting Algorithm :
    An out-place algorithm is an algorithm that needs an extra space in order to produce the output, hence the name is "out-place". 
</pre>

So out-place sorting needs an extra space in the memory and sort the array using the extra space that is allocated to program.