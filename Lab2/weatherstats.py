# #######################
# Studend ID : 112122980
# Name : Mingqian Gao
# #########################

def maximum(lists):
    # To compare each of current element and next element and assign the greater one to next.
    # The maximal element must be stored in the last address of the list.
    for i in range(len(lists) - 1):
        if lists[i] > lists[i+1]:
            lists[i+1] = lists[i]
    return lists[-1]

def average(lists):
    # To calculate the mean of total value of the list.
    sum = 0
    for i in range(len(lists)):
        sum += lists[i]
    return sum/(len(lists))

# Use list to avoid input 12 times and also good for address the data when applying above functions.
rawList = input("Enter twelve numbers representing the rainfall ")
lists = list(map(int, rawList.split()))


print("The maximum is: {}".format(maximum(lists)))
print("The average is: {}".format(average(lists)))

