""" heap_sort.py
https://en.wikipedia.org/wiki/Heapsort
Best O(n) / O(n log n)
Avg O(n log n)
Worst O(n log n)
Space O(1)
21, Oct, 2018
Daniel Hu
"""
import math


def heap_sort(arr):
    n = len(arr)
    heapify(arr, n)
    end = n - 1

    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        sift_down(arr, 0, end)

    return arr


def heapify(arr, n):
    start = i_parent(n-1)

    while start >= 0:
        sift_down(arr, start, n-1)
        start -= 1


def sift_down(arr, start, end):
    root = start

    while i_left_child(root) <= end:
        child = i_left_child(root)
        swap = root

        if arr[swap] < arr[child]:
            swap = child
        if child+1 <= end and arr[swap] < arr[child+1]:
            swap = child + 1
        if swap == root:
            return
        else:
            arr[swap], arr[root] = arr[root], arr[swap]
            root = swap


def i_parent(i):
    return math.floor((i-1) / 2)


def i_left_child(i):
    return 2*i + 1


def i_right_child(i):
    return 2*1 + 2
