import sys
import stdio

# function to compute the sum of powers
def sum_of_powers(n, k):
    total = 0
    for i in range(1, n + 1):
        total += i**k
    return total

# read command line arguments
n = int(sys.argv[1])
k = int(sys.argv[2])

# compute the sum of powers
result = sum_of_powers(n, k)

# print result
stdio.writeln(result)


...
