import sys
import stdio

# read command line arguments as float
t = float(sys.argv[1])
v = float(sys.argv[2])

# check if t > 50
if t > 50:
    stdio.writeln("Value of t must be <= 50 F")
# check if v <= 3
elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")
else:
    # calculate the wind chill using the formula
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**0.16
    # print the wind value
    stdio.writeln(w)

...
