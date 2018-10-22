""" bubble_sort.py
https://en.wikipedia.org/wiki/Bubble_sort
Best O(n)
Avg O(n^2)
Worst O(n^2)
Space O(1)
16, Oct, 2018
Daniel Hu
"""


def bubble_sort(arr):
    n = len(arr)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                new_n = i
        n = new_n

    return arr
