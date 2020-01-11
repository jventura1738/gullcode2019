# Justin Ventura
# 01/11/20
# countdown.py
# Gull Code 2019

monthValues = {
	1: 31,
	2: 28,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10: 31,
	11: 30,
	12: 31,
}

def isLeapYear(Y):
	if Y % 4 == 0 and Y % 100 != 0:
		return True
	elif Y % 4 == 0 and Y % 100 == 0:
		if Y % 400 == 0:
			return True
		else:
			return False

def yearsToDays(Y):
	days = 0
	if Y <= 2020:
		return -1
	else:
		for i in range(2020, Y):
			if isLeapYear(i):
				days += 366
			else:
				days += 365
		return days


import sys
Y, M, D = map(int, sys.stdin.readline().split())

# -1 for special case
count = int(yearsToDays(Y))
if count == -1:
	if Y == 2019:
		if M == 11:
			count += (D - 15)
		else:
			count += (15 + D)
	else:
		count += 46
		monthValues[2] = 29
		for i in range(1, M):
			count += monthValues[i]
		count += (D - 1)
else:
	count += 46
	if isLeapYear(Y):
		monthValues[2] = 29
	for i in range(1, M):
		count += monthValues[i]
	count += (D - 1)

print(count)
