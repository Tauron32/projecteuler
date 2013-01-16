# Smallest multiple
number = 20

def firstFactor(n):
	div = 2
	while n % div != 0 and div <= n:
		div += 1
	return div

def primeFactors(n):
	primeList = []
	new = n
	factor  = firstFactor(new)
	primeList.append(factor)
	while (factor != new):
		new = new/factor
		factor = firstFactor(new)
		primeList.append(factor)
	return primeList

def mcm(args):
	factors = []
	theFactorOfANumber = []
	result = 1
	
	for i in args:
		theFactorOfANumber = primeFactors(i)
		num = theFactorOfANumber[-1]
		while factors.count(num) < theFactorOfANumber.count(num):
			factors.append(theFactorOfANumber.pop())
	for i in factors:
		result *= i
	return result

listNumber = range(2,number+1)
print mcm(listNumber)