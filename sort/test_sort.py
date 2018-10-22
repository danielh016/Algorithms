""" test_sort.py
The testing file for the algorithms
16, Oct, 2018
Daniel Hu
"""


import random
import time

from bubble_sort import bubble_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from heap_sort import heap_sort

arr = []
n = 10000

# Randomly appending an number of items(integer) into the stream
for i in range(0, n):
    arr.append(random.randint(0, 1000))

# Print the randomised stream of integers
print("Original: " + str(arr))


def test_bubble():
    bubble_arr = arr[:]
    start = time.time()
    print("\nBubble Sort: " + str(bubble_sort(bubble_arr)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


def test_quick():
    quick_arr = arr[:]
    start = time.time()
    print("\nQuick Sort: " + str(quick_sort(quick_arr, 0, n-1)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


def test_insertion():
    insertion_arr = arr[:]
    start = time.time()
    print("\nInsertion Sort: " + str(insertion_sort(insertion_arr)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


def test_selection():
    selection_arr = arr[:]
    start = time.time()
    print("\nSelection Sort: " + str(selection_sort(selection_arr)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


def test_merge():
    merge_arr = arr[:]
    start = time.time()
    print("\nMerge Sort: " + str(merge_sort(merge_arr)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


def test_heap():
    heap_arr = arr[:]
    start = time.time()
    print("\nHeap Sort: " + str(heap_sort(heap_arr)))
    end = time.time()
    print("Runtime: " + str("%.5f" % (end - start)) + " sec")


test_bubble()
test_quick()
test_insertion()
test_selection()
test_merge()
test_heap()
