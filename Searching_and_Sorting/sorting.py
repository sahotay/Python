#!/usr/local/bin/python3

'''
1. Bubble Sortt
2. Selection Sort
3. Insertion Sort
4. Shell Sort
5. Merge Sort
6. Quick Sort

Check out the resources below for a review of Bubble sort!

Wikipedia - https://en.wikipedia.org/wiki/Bubble_sort
Visual Algo - https://visualgo.net/en/sorting?slide=1
Animation - http://www.cs.armstrong.edu/liang/animation/web/BubbleSort.html
Sorting Algorithms Animcation with Pseudocode - https://www.toptal.com/developers/sorting-algorithms/bubble-sort
'''
arr = [3,2,13,4,6,5,7,8,1,20]

## Bubble Sort
def bubble_sort(arr):
    # For every element (arranged backwards)
    for n in range(len(arr)-1,0,-1):
        for k in range(n):
            # If we come to a point to switch
            if arr[k]>arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr

# print(list(range(len(arr)-1,0,-1)))
print(f"Sorted list by using bubble_sort: {bubble_sort(arr)}")


## Selection Sort
'''
The selection sort improves on the bubble sort by making 
only one exchange for every pass through the list. 
In order to do this, a selection sort looks for the largest value as
it makes a pass and, after completing the pass, 
places it in the proper location. As with a bubble sort, 
after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. 
This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1) st pass.
'''
def selection_sort(arr):
    for fillslot in range(len(arr)-1,0,-1):
        pos_max = 0
        for location in range(1, fillslot+1):
            if arr[location]>arr[pos_max]:
                pos_max = location
        temp = arr[fillslot]
        arr[fillslot] = arr[pos_max]
        arr[pos_max] = temp
    return arr

print(f"Sorted list by using selection_sort: {selection_sort(arr)}")

## Insertion Sort
'''
Insertion Sort builds the final sorted array (or list) one item at a time.
It is much less efficient on large lists than more advanced algorithms such 
as quicksort, heapsort, or merge sort.
'''
def insertion_sort(arr):
    # For every index in array
    for i in range(1,len(arr)):
        # Set current values and position
        currentValue = arr[i]
        position = i
        # Sorted Sublist
        while position>0 and arr[position-1]>currentValue:
            arr[position]=arr[position-1]
            position = position-1
        arr[position]=currentValue
    return arr

print(f"Sorted list by using insertion_sort: {insertion_sort(arr)}")

## Shell Sort
'''
The shell sort improves on the insertion sort by breaking
the original list into a number of smaller sublists, 
each of which is sorted using an insertion sort. 
The unique way that these sublists are chosen is the key 
to the shell sort. Instead of breaking the list into sublists of contiguous items, 
the shell sort uses an increment i, sometimes called the gap, to create a sublist by 
choosing all items that are i items apart.
'''

def shell_sort(arr):
    sublistcount = len(arr)//2
    # While we still have sub lists
    while sublistcount > 0:
        for start in range(sublistcount):
            # Use a gap insertion
            gap_insertion_sort(arr,start,sublistcount)
        # print(f"sublistcount: {sublistcount}")
        # print(f"Array after each iteration: {arr}")
        sublistcount = sublistcount // 2
    return arr

def gap_insertion_sort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):
        currentvalue = arr[i]
        position = i
        # Using the Gap
        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap
        # Set current value
        arr[position]=currentvalue
arr = [45,67,23,45,21,24,7,2,6,4,90]
print(f"Sorted list by using shell_sort: {shell_sort(arr)}")

## Merge Sort
'''
Merge sort is a recursive algorithm that continually splits a list in half. 
If the list is empty or has one item, it is sorted by definition (the base case). 
If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. 
Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the 
process of taking two smaller sorted lists and combining them together into a single, sorted, new list.
'''

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k]=lefthalf[i]
                i+=1
            else:
                arr[k]=righthalf[j]
                j+=1
            k+=1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i+=1
            k+=1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j+=1
            k+=1
    # print(f"Merging: {arr}")
    return arr
print(f"Sorted list by using merge_sort: {merge_sort(arr)}")

## Quick Sort
'''
A quick sort first selects a value, which is called the pivot value. 
Although there are many different ways to choose the pivot value, 
we will simply use the first item in the list. The role of the pivot value 
is to assist with splitting the list. The actual position where the pivot 
value belongs in the final sorted list, commonly called the split point, 
will be used to divide the list for subsequent calls to the quick sort.
'''
def quick_sort(arr):
    quick_sort_help(arr,0,len(arr)-1)
    return arr

def quick_sort_help(arr,first,last):
    if first<last:
        splitpoint = partition(arr,first,last)

        quick_sort_help(arr,first,splitpoint-1)
        quick_sort_help(arr,splitpoint+1,last)


def partition(arr,first,last):
    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp
    return rightmark

print(f"Sorted list by using quick_sort: {quick_sort(arr)}")