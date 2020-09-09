# Insertion sort


**Time Complexity**: $O(n^2)$

**Auxiliary Space**: $O(1)$

**Boundary Cases**: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.



```python
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr
```


```python
insertion_sort([4, 3, 2, 1])



```




    [1, 2, 3, 4]




```python


```
