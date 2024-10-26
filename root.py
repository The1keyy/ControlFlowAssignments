import sys
import stdio

# function to compute the kth root of c using newtons method with fixed iterations
def kth_root(k, c):
    guess = c / k
    for _ in range(20):
        guess = ((k - 1) * guess + c / guess**(k - 1)) / k
    return guess

# read command line arguments
k = int(sys.argv[1])
c = float(sys.argv[2])

# compute the kth root
result = kth_root(k, c)

# print result
stdio.writeln(result)


...
