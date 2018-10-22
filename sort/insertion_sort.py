""" insertion_sort.py
https://en.wikipedia.org/wiki/Insertion_sort
Best O(n)
Avg O(n^2)
Worst O(n^2)
Space O(1)
18, Oct, 2018
Daniel Hu
"""


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        x = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
        i += 1

    return arr
