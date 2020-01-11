# Justin Ventura
# 01/11/20
# 101doors.py
# Gull Code 2019

doors = [1] * 101

for i in range(2, 102):
	for j in range(i-1, 101, i):
		if doors[j] == 0:
			doors[j] = 1
		else:
			doors[j] = 0

n = int(input())

if n == 0:
	for i in range(0, 101):
		print("{0} {1}".format((i + 1), doors[i]))
elif n == 1:
	for i in range(0, 101):
		if doors[i] == 1:
			print("{0} {1}".format((i + 1), doors[i]))
elif n == 2:
	for i in range(0, 101):
		if doors[i] == 0:
			print("{0} {1}".format((i + 1), doors[i]))
