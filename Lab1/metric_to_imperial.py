# #######################
# Studend ID : 112122980
# Name : Mingqian Gao
# #########################

def metres_to_imperial(metres):
    # To throwout a unexpected situation (not perfect for non-numeric input)
    if metres < 0:
        print("The number must be >= 0, please input again")
        # Iterate a function if come across a invalidated input
        metres_to_imperial(float(input('Input a metres number: ')))

    else:
        # To save the converted valued from metres
        inches = int(round((metres * 39.3701), 0))
        print("{} inches".format(inches))
        # To output the calculated values within print(), shorter codes but might not be good for reading.
        print("{} feet and {} inches".format((inches // 12), (inches % 12)))


metres_to_imperial(float(input('Input a metres number: ')))

