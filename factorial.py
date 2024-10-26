import sys
import stdio

# function to compute the factorial of n
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# read command line argument
n = int(sys.argv[1])

# Compute the factorial
result = factorial(n)

# print the result
stdio.writeln(result)

...
