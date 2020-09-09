# Selection sort

**Time Complexity**: $O(n^2)$ as there are two nested loops.

**Auxiliary Space**: $O(1)$



```python
def selection_sort(arr):
    new_arr = arr
    for i in range(len(new_arr)):
        min_index = i
        for j in range(i + 1, len(new_arr)):
            if new_arr[j] < new_arr[min_index]:
                min_index = j
        new_arr[i], new_arr[min_index] = new_arr[min_index], new_arr[i]
    return new_arr
```


```python
print(selection_sort([4, 5, 1, 3, 2]))
```

    [1, 2, 3, 4, 5]



```python


```
