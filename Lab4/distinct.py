__author__ = 'GaryGoh'


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


def distinct_trick(s):
    # a python inner function that distinct elements in a list
    # It is a trick anyway.
    return ''.join(list(set(s)))


s = input("Input a list:")
print(distinct(s))