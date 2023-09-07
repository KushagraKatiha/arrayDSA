# Sorting Methods 
In this modulde we will discuss about different methods of sorting , how they work what is the time and space complexities involved in them etc 

## Bubble Sort 
Illustration => We have to sort the given array into increasing order using bubble sort
<pre>
Array => arr = [70, 20, 50, 30, 90, 5, 15] 
</pre>

#### Working of Bubble Sort

In bubble sort we compare the two adjacent elements if they are in wrong order we swap them in right order.  

In the given array in Zeroth round =>   

`We started from zero because the indexing in most of the language starts from zero `

<pre>
First element i.e. 70 , compare it with Second element i.e. 20 

The order is not correct, swap it

20, 70 

Now compare Second element i.e. 70 with next element i.e. 50

The order is not correct, swap it

20, 50, 70

Now compare Third element i.e. 70 with the next element i.e. 30

The order is not correct, swap it 

20, 50, 30, 70

Now compare Forth element i.e. 70 with the next element i.e. 90 

The order is correct, don't swap

20, 50, 30, 70, 90

Now compare Fifth element i.e. 90 with the next element i.e. 5

The order is not correct, swap it

20, 50, 30, 70, 5, 90

Now compare Sixth element i.e. 90 with the next element i.e. 15 

The order is not correct, swap it

20, 50, 30, 70, 5, 15, 90

</pre>

After Zeroth round of comparison we got  `arr = [20, 50, 30, 70, 5, 15, 90]`  

Here we can see that the right most element is at correct position so now we do not have to compare it with any element , now we have to traverse the only till second last element

First Round =>  `arr = [20, 50, 30, 70, 5, 15, 90]`

<pre>
First element i.e. 20 , compare it with Second element i.e. 50 

The order is correct, don't swap it

20, 50

Now compare Second element i.e. 50 with next element i.e. 30

The order is not correct, swap it

20, 30, 50

Now compare Third element i.e. 50 with the next element i.e. 70

The order is correct, don't swap it 

20, 30, 50, 70

Now compare Forth element i.e. 70 with the next element i.e. 5

The order is not correct, swap it

20, 30, 50, 5, 70

Now compare Fifth element i.e. 70 with the next element i.e. 15

The order is not correct, swap it

20, 30, 50, 5, 15, 70

</pre>

After First round of comparison we got  `arr = [20, 30, 50, 5, 15, 70, 90]` 

Here we can see that the right most element and 2nd last element is at correct position so now we do not have to compare them with any element , now we have to traverse the only till third last element


Similarly After <b>Second round</b> we will get array `arr = [20, 30, 5, 15, 50, 70, 90]`

After <b>Third round</b> we will get array `arr = [20, 5, 15, 30, 50, 70, 90]`  

After <b>Forth round</b> we will get array `arr = [5, 15, 20, 30, 50, 70, 90]`  




### Here we can observe that => 

How we traversed in each round (or pass) => 

<pre>
let len(arr) = n

Zeroth round [70, 20, 50, 30, 90, 5, 15]        n
               -   -   -   -   -  -   -  

First round [20, 50, 30, 70, 5, 15, 90]         (n-1)
              -   -   -   -   -   -       

Second round [20, 30, 5, 15, 50, 70, 90]        (n-2)
              -   -   -  -   -

Third round [20, 5, 15, 30, 50, 70, 90]         (n-3)
             -   -   -   - 

Forth round [5, 15, 20, 30, 50, 70, 90]         (n-4) = 3
             -   -  -  

Fifth round [5, 15, 20, 30, 50, 70, 90]         (n-5) = 2
             -   -  
             
Sixth round [5, 15, 20, 30, 50, 70, 90]         (n-6) = 1
             -  
</pre>

We can here observe that:  

<pre>
length of array (n) = 7  
passes required (p) = 6

<pre>
Generally saying p = n-1
</pre>

Comparisions in worst case => n + (n-1) + (n-2) + ...... + 3 + 2 + 1
which is nothing else but sum of n natural numbers i.e. {n(n+1)}/2

Comparisons in worst case => O(n^2)  
Similarly, Swaps in worst case => O(n^2)            

Time Complexity = Comparison + Swaps
O(n^2)          =  O(n^2)   +  O(n^2) 

And since we are using no extra space , space complexity will be => O(1) {constant}      
</pre>


## Implementation Code of Bubble Sort

<pre>
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
   return arr        

arr = [70, 20, 50, 30, 90, 5, 15]

bSortResult = bubbleSort(arr)
print("After applying bubble  =>",bSortResult)

// Output : After applying bubble  => [5, 15, 20, 30, 50, 70, 90]
</pre>