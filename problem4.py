# Largest palindrome product
result = 0
stop = False
number1, number2 = 0, 0

def isPalindrome(n):
	numberString = str(n)
	return numberString == numberString[::-1]

while number1 < 1000:
	number2 = number1
	while number2 < 1000:
		new = number1 * number2
		if isPalindrome(new) and new > result:
			result = new
		number2 += 1
	number1 += 1

print "Result: ", result