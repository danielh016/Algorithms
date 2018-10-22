""" test_sampler.py
22, Oct, 2018
Daniel Hu
"""


import random
from Reservoir import Reservoir

k = 10  # sample size
stream = []  # record the actual stream, for testing purpose

res_sample = Reservoir(k)  # new reservoir class

for i in range(0, 100):
    num = int(random.uniform(1, 1001))  # randomly generate the stream
    stream.append(num)
    res_sample.add(num)

print("Actual Stream: " + str(stream))
print("\nSampled " + str(k) + " items: " + str(res_sample.sample()))
