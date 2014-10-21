# #######################
# Studend ID : 112122980
# Name : Mingqian Gao
# #########################

def calc_amount(principal, rate, duration):
    # An iteration way to calculate the result in each stage when duration is validated
    while duration > 0:
        return calc_amount(principal*(1+rate), rate, duration - 1)
    return principal



principal = int(input("principal "))
rate = float(input("rate "))
duration = int(input("duration "))

print("{}".format(calc_amount(principal, rate, duration)))