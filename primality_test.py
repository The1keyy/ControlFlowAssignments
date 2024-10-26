import sys
import stdio

# function to check if n is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# read command line argument
n = int(sys.argv[1])

# check if n is prime
result = is_prime(n)

# print the result
stdio.writeln(result)


...
