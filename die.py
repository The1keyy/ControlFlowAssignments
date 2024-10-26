import stdio
import stdrandom

# roll the die by generating a random number that an integer between 1 and 6
roll = stdrandom.uniformInt(1,7)

# print the pattern
if roll == 1:
    stdio.writeln("*")
elif roll == 2:
    stdio.writeln("* *")
elif roll == 3:
    stdio.writeln("* *\n *")
elif roll == 4:
    stdio.writeln("* *\n* *")
elif roll == 5:
    stdio.writeln("* *\n * \n* *")
elif roll == 6:
    stdio.writeln("* *\n* *\n* *")


...
