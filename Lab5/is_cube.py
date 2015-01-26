__author__ = 'GaryGoh'


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


print(is_cube(int(input())))