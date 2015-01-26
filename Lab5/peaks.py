__author__ = 'GaryGoh'


def peaks(s):
    # Empty list
    if not s:
        return []

    # Not emtpy list
    # initialized ascList in order to avoid list index out of range
    ascList = [s[0]]

    # Similar as insertion sort, but no need to walk though the new list again
    # Only compare the current element from original list to the latest element from new list
    # This way can have O(n) = n time consuming
    for i in s:
        if i > ascList[-1]:
            ascList.append(i)
    return ascList


rawList = input()
lists = list(map(int, rawList.split()))

print(peaks(lists))


