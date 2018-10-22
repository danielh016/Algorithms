""" merge_sort.py
https://en.wikipedia.org/wiki/Merge_sort
Using bottom-up implementation
Best O(n log n)
Avg O(n log n)
Worst O(n log n)
Space O(n)
20, Oct, 2018
Daniel Hu
"""


def merge_sort(arr):
    def doubling_range(start, end):
        while start < end:
            yield start
            start *= 2

    def merging(arr, i_left, i_right, i_end, working_arr):
        i = i_left
        j = i_right
        for k in range(i_left, i_end):
            if i < i_right and (j >= i_end or arr[i] <= arr[j]):
                working_arr[k] = arr[i]
                i += 1
            else:
                working_arr[k] = arr[j]
                j += 1

    def copy_array(arr, working_arr, n):
        for i in range(0, n):
            arr[i] = working_arr[i]

    working_arr = []
    n = len(arr)
    for i in range(0, n):
        working_arr.append(arr[i])
    for width in doubling_range(1, n):
        for i in range(0, n, 2 * width):
            merging(arr, i, min(i+width, n), min(i+2*width, n), working_arr)
        copy_array(arr, working_arr, n)

    return arr
