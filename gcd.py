import sys
import stdio

# compute the gcd using the euclidean algorithm
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

# command line arguments for p and q
p = int(sys.argv[1])
q = int(sys.argv[2])

# compute the gcd
result = gcd(p, q)

# print the result
stdio.writeln(result)


...
