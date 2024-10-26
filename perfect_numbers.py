import sys
import stdio

# function to check if a number is perfect
def is_perfect(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum == num

# function to find all perfect numbers less than or equal to n
def find_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n + 1):
        if is_perfect(i):
            perfect_numbers += [i]
    return perfect_numbers

# read command line argument
n = int(sys.argv[1])

# find perfect numbers less than or equal to n
perfect_numbers = find_perfect_numbers(n)

# print the perfect numbers
for number in perfect_numbers:
    stdio.writeln(number)


...
