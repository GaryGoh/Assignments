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


print(read_dictionary('test.txt'))