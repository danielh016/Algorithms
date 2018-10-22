""" quick_sort.py
https://en.wikipedia.org/wiki/Quicksort
Best O(n log n)
Avg O(n log n)
Worst O(n^2) -> due to the poor choice of pivot
we can avoid this by choosing pivots uniformly at random.
We will come back after implementing the hash function and solve this problem.
Finally, we will get and expected running time of O(n log n)
Space O(log n) -> O(n)
17, Oct, 2018
Daniel Hu
"""


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p-1)
        quick_sort(arr, p+1, high)

    return arr


def partition(arr, low, high):
    def swap(a, b):
        arr[a], arr[b] = arr[b], arr[a]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            if i != j:
                swap(i, j)
            i += 1
    swap(i, high)

    return i

