__author__ = 'GaryGoh'

def inverse(d):
    # new a dictionary and store as {value: key}
    inverse_d = {}

    for (key, value) in d.items():
            inverse_d[value] = key
    return inverse_d

d = {'sun': 'grian', 'tree': 'crann', 'horse': 'capall', 'water': 'uisce'}

print(inverse(d))