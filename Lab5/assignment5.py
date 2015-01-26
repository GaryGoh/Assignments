__author__ = 'GaryGoh'


def peaks(s):
    # Empty list
    if not s:
        return []

    # Not emtpy list
    # initialized ascList in order to avoid list index out of range
    ascList = [s[0]]

    # Similar as insertion sort, but no need to walk though the new list again
    # Only compare the current element from original list to the latest element from new list
    # This way can have O(n) = n time consuming
    for i in s:
        if i > ascList[-1]:
            ascList.append(i)
    return ascList


def is_cube(n):
    # Since cube function is symmetric then get the absolute value to break symmetric
    n = abs(n)

    # A simple way with O(n) = n
    # Just test the number from 0 to objective number if exist a number i, i ^ 3 = objective number
    for i in range(0, n + 1):
        if i ** 3 > n:
            return False
        elif i ** 3 == n:
            return True
    return False

def first_cube_above(n):
    # only return lower bound of the cube root of n, then calculate the cube of the result + 1
    return int(n ** (1 / 3.0) + 1) ** 3


