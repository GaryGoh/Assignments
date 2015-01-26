__author__ = 'GaryGoh'

# Q1
# Write a Python function Firsts(s) to return the string formed
# from the first occurrence of each item in string s.

def First(s):
    first_list = []

    for i in s:
        if not (i in first_list):
            first_list.append(i)
    return ''.join(first_list)


# Q2
# Write a Python function IsStairs( s ) to test if the numeric list s
# is a stairs ( a stairs is a list of at least two numbers where either
# each number is one greater than the previous number or each number is
# one smaller than the previous number ).

def IsStairs(s):
    if len(s) < 2:
        return False
    else:
        stairs_list = []

        for i in range(s[0], s[-1] + (s[-1] - s[-2]), s[1] - s[0]):
            stairs_list.append(i)
        return s == stairs_list

# Q3
# Write a Python function LineCount(filenames) to take a list filenames of file
# names and write out each file name and the number of lines in that file,
# finally writing out the total number of lines in all files. Assume that
# each file name has at most 20 characters, and that the total number of lines
# is at most 999,999. If any of the files cannot be read, then issue an appropriate
# error message and otherwise ignore that file.

def LineCount(filenames):
    file_dic = {}
    total_num = 0

    for i in filenames:
        if len(i) > 20:
            file_dic[i] = "cannot read file"
        else:
            inputfile = open(i, 'r')
            line_num = 0
            while True:
                line = inputfile.readline()
                line_num += 1

                if line == "":
                    break
            if line_num > 999999:
                file_dic[i] = "cannot read file"
            else:
                file_dic[i] = line_num
    for i in file_dic:
        total_num += file_dic[i]
        print("%s  %d" % (i, file_dic[i]))
    print("TOTAL  %d" % (total_num))

    return


# Q4
# Write a Python function Counts(s) to return a dictionary, in which each key is a distinct
# item in sequence s and the corresponding value is the number of times that the item occurs
# in s; for efficiency, this function should inspect each item in s only once.

def Counts(s):
    s_dic = {}

    for i in s:
        s_dic[i] = s.count(i)
        # Knocked out the item just came up.
        filter(lambda l: l != i, s)
    return s_dic


# Write a Python function MostFrequent(s) to return an item in the non-empty sequence s which
# occurs at least as many times as every other such item.

def MostFrequent(s):
    s = Counts(s)
    # Straightforwardly return the last item of sorted values,
    # which counts the number of occurrences ot each item.
    for i in s.keys():
        if s[i] == sorted(s.values())[-1]:
            return i


# Write a Python function AreAnagrams(s1,s2) to test if sequences s1 and s2 are anagrams of one
# another (anagrams contain the same overall collection of items, but perhaps in different orders ).

def AreAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        # sorting them then compare both.
        s1 = sorted(s1)
        s2 = sorted(s2)
        logi = True
        for i in map(lambda l1, l2: bool(l1 == l2), s1, s2):
            logi &= i
    return logi
