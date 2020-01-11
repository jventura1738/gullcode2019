# Justin Ventura
# 01/11/20
# outofboxadd.py
# Gull Code 2019

import sys
a,b = map(int, sys.stdin.readline().split())

if a >= 0:
	if b >= 0:
		for i in range(0, b):
			a += 1
		print(a)
	else:
		for i in range(0, b, -1):
			a -= 1
		print(a)
elif a < 0:
	if b >= 0:
		for i in range(0, b):
			a += 1
		print(a)
	else:
		for i in range(0, b, -1):
			a -= 1
		print(a)