""" test_sim.py
Testing the distance and similarity algorithms
18, Oct, 2018
Daniel Hu
"""

from euclidean_distance import euclidean_distance
from manhattan_distance import manhattan_distance
from cosine_similarity import cosine_similarity

vector_a = [1, 3, 4, 5]
vector_b = [1, 2, 3, 4]

print(euclidean_distance(vector_a, vector_b))
print(manhattan_distance(vector_a, vector_b))
print(cosine_similarity(vector_a, vector_b))
