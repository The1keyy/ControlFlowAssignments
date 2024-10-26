import sys
import stdio

# command line input handling
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Check if a is zero
if a == 0:
    stdio.writeln("Value of a must not be 0")  # output an error message
else:
    # calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    # check if the discriminant is negative
    if discriminant < 0:
        stdio.writeln("Value of discriminant must not be negative")
    else:
        # calculate the two roots using the quadratic formula
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)

        # print the result
        stdio.writeln(str(root1) + " " + str(root2))

...
