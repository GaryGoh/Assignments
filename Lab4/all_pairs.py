__author__ = 'GaryGoh'


def all_pairs(s1, s2):
    # traversing each list and print them, O(n) = n^2.
    # There might be a better way but this way is the most straightforward
    for i in s1:
        for j in s2:
            print(i, j)
    return


s1 = input("Input the first list: ")
s2 = input("Input the second list")

all_pairs(s1, s2)
