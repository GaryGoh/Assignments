__author__ = 'GaryGoh'


def search_file(filename, target):
    file = open(filename, "r")
    line_num = 0

    while True:
        # read each line of file
        line = file.readline()
        line_num = line_num + 1

        # To output the line contains target words
        if line.find(target) != -1:
            print("%3d − %s" % (line_num, line), end="")

        # To break the dead loop
        if line == "":
            break
    return


print(search_file("testFile.txt", "the"))