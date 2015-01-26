__author__ = 'GaryGoh'


def squeeze(filename):
    file = open(filename, "r")
    line_num = 0
    preLine = ""

    while True:
        line = file.readline()
        # To break dead loop
        if line == "":
            break
        line_num = line_num + 1

        # Compare with previous line if same as current line
        if line != preLine:
            print("%3d - %s" % (line_num, line))
        # To store the previous line because it is hard to get the previous line after pointer moving to next
        preLine = line
    return


print(squeeze("test2File.txt"))