import random

def play():
    diceList = [-1]
    while True:
        diceList = diceList + [random.randint(1,6)]
        if (diceList[-1] == 6) and (diceList[-2] == diceList[-1]):
            for i in range(1, len(diceList)):
                print("{} ".format(diceList[i]), end="")
            return len(diceList) - 1
        


throwsDice = []
sum = 0
for i in range(0,20):
    sum = sum + play()
    print("")

print("The mean of 20 times games of throws is: {}".format(sum/24))



