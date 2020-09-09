# Merge sort

**Time Complexity**: $O(nlog(n))$

**Auxiliary Space**: $O(n)$


```python
def merge_sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        l = arr[:mid] # Dividing the array elements 
        r = arr[mid:] # into 2 halves 

        merge_sort(l) # Sorting the first half 
        merge_sort(r) # Sorting the second half 

        i = j = k = 0
        while i < len(l) and j < len(r):  
            if l[i] < r[j]: 
                arr[k] = l[i] 
                i+= 1
            else: 
                arr[k] = r[j] 
                j+= 1
            k+= 1
            
        while i < len(l): 
            arr[k] = l[i] 
            i+= 1
            k+= 1
            
        while j < len(r): 
            arr[k] = r[j] 
            j+= 1
            k+= 1
    return arr
```


```python
merge_sort([4, 3, 2, 1])
```




    [1, 2, 3, 4]




```python


```
