# #######################
# Studend ID : 112122980
# Name : Mingqian Gao
# #########################

def square(n):
    # Throwout the unexpected situation, still not perfect for non-numeric value
    if n <= 0:
        print("Please input a positive integer number")
        square(int(input("Enter a positive integer value n:")))

    else:
        # Outer for loop is to print how many rows in there
        for i in range(0, n):
            # Inner for loop is to print each row *
            for j in range(0, n):
                print('*', end='')
            print()


square(int(input("Enter a positive integer value n:")))
