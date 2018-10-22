""" morris_counter
Basic counter, do increment function per stream items comes in.
Only needs to store the "counter" variable (memory efficient)
Returns 2^counter - 1
Can be improved by measuring the median of multiple executions.
We can then get an accuracy of more than 3/4 of the estimation
23, Oct, 2018
Daniel Hu
"""


import random


class MorrisCounter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        r = random.uniform(0, 1)
        p = 2 ** self.counter
        if r < 1/p:
            self.counter += 1

    def count(self):
        return 2**self.counter - 1


n = 64  # times to increment
k = 10  # times to test

counter = []
for i in range(0, k):
    counter.append(MorrisCounter())

for i in range(1, n+1):
    for j in range(0, k):
        counter[j].increment()
        print("actual " + str(i) + ", Morris[" + str(j) + "], counter = " + str(counter[j].count()))
