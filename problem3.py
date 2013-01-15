# Largest prime factor
number = 600851475143
i = 2
result = 0
stop = False

def isPrime(n):
	i = 2
	result = True
	while i < n/2 and result:
		if n % i == 0:
			result = False
		i = i + 1
	return result

while i < number/2 and not stop:
	if number % i == 0:
			result = number/i
			if isPrime(result):
				stop = True
	i = i + 1

print "Result: ", result