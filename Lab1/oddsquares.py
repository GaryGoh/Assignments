§########################
# Studend ID : 112122980
# Name : Mingqian Gao
##########################


def oddsquares(n):
    # Throwout the unexpected situation, still not perfect for non-numeric value
    if n < 0:
        print("Please input a non-negative number and try again")
        oddsquares(int(input("Input a non-negative integer number:")))

    else:
        sum = 0
        # no need to judge if n is odd just set a interval of 2 from 1
        for i in range(1, n + 1, 2):
            sum += i ** 2
        print("Sum:{}".format(sum))
    return


oddsquares(int(input("Input a non-negative integer number:")))
