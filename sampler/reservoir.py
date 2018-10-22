""" reservoir.py
A randomized algorithm for choosing a sample of k items from a list S containing n items,
where n is either a very large or unknown number -- cited from Wikipedia
https://en.wikipedia.org/wiki/Reservoir_sampling
input: stream
output: a sample item
22, Oct, 2018
Daniel Hu
"""


import random

class reservoir():
    def __init__(self, k, m=0, arr=[]):
        self.k = k  # sample size
        self.m = m  # stream length count
        self.arr = arr  # sample

    def add(self, item):
        self.m += 1
        if self.m <= self.k:
            self.arr.append(item)
        else:
            i = int(random.uniform(0, self.m))
            if i < self.k:
                self.arr[i] = item

    def sample(self):
        return self.arr
