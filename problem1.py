# -*- coding:utf-8 -*-
# Constants and variables
MAX = 1000
multiples = []
result = 0

# The main program
for i in range(1, MAX):
	if i % 3 == 0:
		multiples.append(i)
	elif i % 5 == 0:
		multiples.append(i)

for j in multiples:
	result += j
	
print "Result: ", result
