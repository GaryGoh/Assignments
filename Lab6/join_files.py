__author__ = 'GaryGoh'


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

ins = ["test2File.txt", "testFile.txt"]

print(join_files(ins, "outputFile"))