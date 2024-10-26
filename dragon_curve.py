import sys
import stdio

# function to generate the dragon curve
def dragon_curve(n):
    if n == 0:
        return "F"

    # recursive step
    previous_curve = dragon_curve(n - 1)

    # reverse the previous curve and manually swap l with r and vice versa
    reversed_curve = ""
    for char in previous_curve[::-1]:
        if char == "L":
            reversed_curve += "R"
        elif char == "R":
            reversed_curve += "L"
        else:
            reversed_curve += char

    # return the new curve
    return previous_curve + "L" + reversed_curve

# read command line argument for n
n = int(sys.argv[1])

# get the dragon curve instructions
instructions = dragon_curve(n)

# print the instructions
stdio.writeln(instructions)

...
