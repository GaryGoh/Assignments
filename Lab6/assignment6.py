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


def join_files(inputfilenames, outputfilename):
    outputfile = open(outputfilename, "w")

    for inputfilename in inputfilenames:
        inputfile = open(inputfilename, "r")
        # To get each line and write into the outputfile
        while True:
            line = inputfile.readline()
            if line == "":
                break
            outputfile.write(line)
        # To break different line with previous file
        outputfile.write("\n")

    # is to test the outputfile
    # while True:
    #     line = outputfile.readline()
    #     if line == "":
    #         break
    #     print("%s" % (line))

    return