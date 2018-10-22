""" selection_sort.py
https://en.wikipedia.org/wiki/Selection_sort
Best O(n^2)
Avg O(n^2)
Worst O(n^2)
Space O(1)
19, Oct, 2018
Daniel Hu
"""


def selection_sort(arr):
    n = len(arr)

    for j in range(0, n-1):
        i_min = j
        for i in range(j+1, n):
            if arr[i] < arr[i_min]:
                i_min = i
        # swap
        if i_min != j:
            arr[j], arr[i_min] = arr[i_min], arr[j]

    return arr
