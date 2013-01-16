# 10001st prime
def isPrime(n):
	i = 2
	result = True
	while i <= n/2 and result:
		if n % i == 0:
			result = False
		i = i + 1
	return result

magicNumber = 10001
cont = 0
i = 2
while cont < magicNumber:
	if isPrime(i):
		cont += 1
	i += 1

print i-1