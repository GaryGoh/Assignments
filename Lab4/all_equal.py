__author__ = 'GaryGoh'


def all_equal(s):
    # only need to compare the length of each element if greater then 1
    for i in s:
        if s.count(i) > 1:
            return False
    return True


rawList = input("Input a list with any type of elements")

print(all_equal(rawList))