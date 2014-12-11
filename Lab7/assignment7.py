__author__ = 'GaryGoh'


def read_dictionary(filename):
    file = open(filename, "r")
    # init a dictionary
    r_dict = {}
    for line in file:
        # Add a new enry with the key = line.split()[0]
        # line.split() will return a list then just locate values with numeric index
        r_dict[line.split()[0]] = line.split()[1]
    return r_dict


def print_dictionary(d):
    # abstract keys of d and sort them
    # I suppose left-justified columns of width 10 is that
    # each column has 10 width from left to right.
    for k in sorted(d.keys()):
        print("%-10s : %-10s" % (k, d[k]))
    return


def inverse(d):
    # new a dictionary and store as {value: key}
    inverse_d = {}

    for (key, value) in d.items():
        inverse_d[value] = key
    return inverse_d

