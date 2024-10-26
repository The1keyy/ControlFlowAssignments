import sys
import stdio

# function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# function to count the number of primes less than or equal to n
def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

# read command line argument
n = int(sys.argv[1])

# compute the number of primes less than or equal to n
result = count_primes(n)

# print the result
stdio.writeln(result)

...
