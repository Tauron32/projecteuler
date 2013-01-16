# Sum square difference
def sumSquares(args):
	result = 0
	for i in args:
		result += (i*i)
	return result

	
def squareSums(args):
	result = 0
	for i in args:
		result += i
	return result*result

myRange = range(1,101)
print squareSums(myRange) - sumSquares(myRange)