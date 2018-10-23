""" misra-gries.py
Tracking the k most frequent item of the stream (the majority)
https://en.wikipedia.org/wiki/Misra-Gries_summary
24, Oct, 2018
Daniel Hu
"""


class MisraGries:
    def __init__(self, k):
        self.k = k  # k-1 is the items we are keeping track of.
        self.dict = {}  # tracking item pairs (item: freq)
        self.m = 0  # keep track of the total items in the stream

    def add(self, item):
        self.m += 1
        if item in self.dict:
            self.dict[item] += 1
        else:
            if len(self.dict) < self.k - 1:
                self.dict[item] = 1  # put the key into dict with value 1
            else:
                marked = []
                for key in self.dict.keys():
                    self.dict[key] -= 1
                    if self.dict[key] <= 0:
                        marked.append(key)
                for key in marked:
                    del self.dict[key]

    def find_majority(self):
        for key in self.dict.keys():
            print("Item " + str(key) + "'s frequency: " + str(self.dict[key]))


misra_gries = MisraGries(3)
stream = ['T', 'D', 'D', 'C', 'D', 'C', 'C', 'D', 'M', 'D']
# T=1, D=5, C=2,  M=1
for item in stream:
    misra_gries.add(item)

misra_gries.find_majority()
