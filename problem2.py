#Constants and variables
MAX = 4000000
result, a, b = 0, 1, 2
# Main program
while b < MAX:
	if b % 2 == 0:
		result += b
	a, b = b, a+b

print "Result: ", result