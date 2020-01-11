# Justin Ventura
# 01/11/20
# NthPrime.py
# Gull Code 2019

from math import sqrt

def NthPrime(n):
	if n == 1: return 2
	elif n == 2: return 3
	elif n == 3: return 5

	curr = 3
	val = 7
	while (curr <= n):
		if isPrime(val):
			curr += 1
		if curr == n:
			return val
		else:
			val += 2

def isPrime(n):
	if n % 2 == 0:
		return false
	buffer = int(sqrt(n))
	buffer += 1

	for i in range(3, buffer, 2):
		if n % i == 0: return False

	return True

# Testing
# N = int(input("Enter an N: "))
# print(NthPrime(N))



