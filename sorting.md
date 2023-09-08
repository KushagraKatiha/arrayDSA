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



## Selection Sort

Illustration => We have to sort the given array into increasing order using bubble sort
<pre>
Array => arr = [70, 20, 50, 30, 90, 4, 15] 
</pre>

#### Working of Bubble Sort

Unlike in bubble sort , in selection sort we don't compare element with adjacent element but we make an variable to store the index of the smallest element present in array. Let's see how do we do this:

<pre>
<pre>

Pass Number (n) = 0

arr = [70, 20, 50, 30, 90, 4, 15]
</pre>
<b>min_idx = n</b> 

Now we will compare arr[mid_idx] is less than any other element in array if yes then we will update the value of 
"min_idx" to the index of that element and after comparing with all the elements we will make a swap within the array

arr[min_idx] = 70 
arr[1] = 20 

arr[1] < arr[min_idx], we will now update the value of min_idx with 1

<b>min_idx = 1</b>
arr[min_idx] = 20
arr[2] = 50 

arr[2] > arr[min_idx], leave it as it is 

arr[3] = 30

arr[3] > arr[min_idx], leave it as it is

arr[4] = 90

arr[4] > arr[min_idx], leave it as it is

arr[5] = 4

arr[5] < arr[min_idx], update the value of min_idx
<b>min_idx = 5</b>

arr[min_idx] = 4
arr[6] = 15

arr[6] > arr[min_idx], leave it as it is

After traversing whole array and comparing we got <b>min_idx = 5</b> , 
now we have to swap arr[min_idx] with arr[n] , so we will be getting the smallest number at very first index i.e. 0

</pre>

So after zeroth pass `arr = [4, 20, 50, 30, 90, 70, 15]`  

We will repeate the complete process as we done above but as we have got smallest element at very first first index i.e. 0 we will now start comparision from 1 (or we will start traversing with number of index same as that of pass)

<pre>
<pre>
Pass Number (n) = 1

arr = [4, 20, 50, 30, 90, 70, 15]
</pre>

As done above, 

arr[min_idx] = 20
arr[2] = 50  

arr[2] > arr[min_idx], leave it as it is

arr[3] = 30 

arr[3] > arr[min_idx], leave it as it is 

arr[4] = 90

arr[4] > arr[min_idx], leave it as it is

arr[5] = 70

arr[5] > arr[min_idx], leave it as it is

arr[6] = 15

arr[6] < arr[min_idx], update the value of min_idx

<b>min_idx = 6</b>


After traversing whole array and comparing we got <b>min_idx = 6</b> , 
now we have to swap arr[min_idx] with arr[n] , so we will be getting the smallest number at very first index i.e. 1 (in this case)


</pre>

So after first pass `arr = [4, 15, 50, 30, 90, 70, 20]`

We can here see that after completing two passes we got first two element sorted, after x = len(arr) passes we will get the complete sorted array try doing the futher steps yourself to get more clarity on the topic:  \

Final sorted array: `arr = [4, 15, 20, 30, 50, 70, 90]`

### Digramatic Understanding

<pre>
<pre>
arr = [70, 20, 50, 30, 90, 4, 15]
</pre>

In Zeroth Pass => arr = [70, 20, 50, 30, 90, 4, 15]           N
                          _   _   _   _   _  _   _

In First Pass => arr = [4, 20, 50, 30, 90, 70, 15]            N-1
                            _   _   _   _   _   _

In Second Pass => arr = [4, 15, 50, 30, 90, 70, 20]           N-2
                                 _   _   _   _   _

In Third Pass => arr = [4, 15, 20, 30, 90, 70, 50]            N-3
                                    _   _   _   _

In Fourth Pass => arr = [4, 15, 20, 30, 90, 70, 50]            3
                                         _   _   _

In Fifth Pass => arr = [4, 15, 20, 30, 50, 70, 90]             2
                                            _   _ 

In Sixth Pass => arr = [4, 15, 20, 30, 50, 70, 90]             1
                                                _
</pre>

### We can observe that 

<pre>
Swaps => We have N-1 number of passes, and in worst case at every pass we are having one swap
therefore, we will have total number or swaps = O(N)

Comparisons => starting with N elements we will have N-1 elements then N-2 elements and so on till 1
therefore, total number of comparisons = {N(N+1)}/2 = O(N^2)

Here Time Complexity = O(N) + O(N^2) => O(N^2)
</pre>

Both bubble sort and Selection sort have time complexities of O(N^2), so the only difference in both or them is of approach we are using in both the sorting methods.
