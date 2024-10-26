import sys
import stdio

# function to compute the n fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_0 = 0  # F(0)
        fib_1 = 1  # F(1)
        for i in range(2, n + 1):
            fib_n = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = fib_n
        return fib_n

# read command line argument
n = int(sys.argv[1])

# compute the fibonacci number
result = fibonacci(n)

# Output the result using stdio.writeln
stdio.writeln(result)


...
