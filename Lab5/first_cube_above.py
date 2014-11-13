__author__ = 'GaryGoh'


def first_cube_above(n):
    # only return lower bound of the cube root of n, then calculate the cube of the result + 1
    return int(n ** (1 / 3.0) + 1) ** 3

print(first_cube_above(int(input())))