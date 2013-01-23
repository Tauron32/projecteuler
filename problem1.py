# -*- coding:utf-8 -*-
# Constants and variables
MAX = 1000
multiples = []
result = 0

# The main program
for i in range(1, MAX):
	if (i % 3 == 0) or (i % 5 == 0):
		result += i
	
print "Result: ", result
