import sys
import stdio

# function to find ramanujan numbers less than or equal to n
def find_ramanujan_numbers(n):
    results = []

    # loop through possible values for a and b
    max_value = int(n ** (1 / 3)) + 1
    for a in range(1, max_value):
        for b in range(a, max_value):
            sum1 = a ** 3 + b ** 3
            if sum1 > n:
                continue

            # loop through possible values for c and d
            for c in range(1, max_value):
                for d in range(c, max_value):
                    sum2 = c ** 3 + d ** 3

                    # if we find two pairs with the same sum and they are distinct
                    if sum1 == sum2 and (a, b) != (c, d):
                        already_found = False
                        for number in results:
                            if number[0] == sum1:
                                already_found = True
                                break

                        if not already_found:
                            index = 0
                            while index < len(results) and results[index][0] < sum1:
                                index += 1
                            results.insert(index, (sum1, a, b, c, d))

    return results

# read command line argument
n = int(sys.argv[1])

# find ramanujan numbers less than or equal to n
ramanujan_numbers = find_ramanujan_numbers(n)

# print the ramanujan numbers
for num, a, b, c, d in ramanujan_numbers:
    stdio.writeln(str(num) + " = " + str(a) + "^3 + " + str(b) + "^3 = " + str(c) + "^3 + " + str(d) + "^3")

...
