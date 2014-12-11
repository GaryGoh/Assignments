__author__ = 'GaryGoh'


# Iteration
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 1)



# Dynamic programing
def fibonacci_dp(n):
    fib_dictionary = [0, 1]
    if n <= 1:
        return 1
    else:
        for i in fib_dictionary:
            if
