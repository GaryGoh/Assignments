__author__ = 'GaryGoh'


def all_equal(s):
    # only need to compare the length of each element if greater then 1
    for i in s:
        if s.count(i) > 1:
            return False
    return True

def all_pairs(s1, s2):
    # traversing each list and print them, O(n) = n^2.
    # There might be a better way but this way is the most straightforward
    for i in s1:
        for j in s2:
            print(i, j)
    return


def distinct(s):
    # Trying to use lazy evaluation but not working so how?
    # distList = []
    # distList = [i for i in s if distList.count(i) < 1]
    #

    # new a list and insert all elements from objective list with a filter that
    # the incoming element shows up once in disList[]
    distList = []
    for i in s:
        if distList.count(i) < 1:
            distList.append(i)
    return ''.join(distList)


# def distinct_trick(s):
#     a python inner function that distinct elements in a list
#     It is a trick anyway.
    # return ''.join(list(set(s)))