""" bigram.py
2-Gram
https://en.wikipedia.org/wiki/N-gram
2018/10/26
Daniel Hu
"""


def bigram(token, correct_word):
    def bi_process(ori):
        new_list = ["#" + ori[0]]
        for i in range(1, len(ori)+1):
            if i == len(ori):
                new_list.append(ori[i-1] + "#")
            else:
                new_list.append(ori[i-1] + ori[i])
        return new_list

    in_list = bi_process(token)
    com_list = bi_process(correct_word)

    intersection = len(set(in_list) & set(com_list))  # store the number of intersections between the two words
    distance = len(in_list) + len(com_list) - (2 * intersection)  # measure the distance between the two words

    return distance
