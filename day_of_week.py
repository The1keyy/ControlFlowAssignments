import sys
import stdio

# command line input handling
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

# calculate y0
y0 = y - (14 - m) // 12

# calculate x0
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400

# calculate m0
m0 = m + 12 * ((14 - m) // 12) - 2

# calculate the day of the week
dow = (d + x0 + (31 * m0) // 12) % 7

# make a lisr of the dow
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print the dow
stdio.writeln(days_of_week[dow])

...
