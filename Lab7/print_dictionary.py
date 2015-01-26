__author__ = 'GaryGoh'

def print_dictionary(d):
    # abstract keys of d and sort them
    # I suppose left-justified columns of width 10 is that
    # each column has 10 width from left to right.
    for k in sorted(d.keys()):
        print("%-10s : %-10s" % (k, d[k]))
    return

d = {'sun': 'grian', 'tree': 'crann', 'horse': 'capall', 'water': 'uisce'}
print_dictionary(d)