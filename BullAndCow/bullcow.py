# Justin Ventura
# 01/11/20
# bullcow.py
# Gull Code 2019

num1 = int(input("1 Enter 4digit integer: "))
num2 = int(input("2 Enter 4digit integer: "))
bull = 0
cow = 0
tlist1 = []
tlist2 = []

for i in range(4):
	temp1 = num1 % 10
	temp2 = num2 % 10
	num1 //= 10
	num2 //= 10
	tlist1.append(temp1)
	tlist2.append(temp2)

	if temp1 == temp2:
		bull += 1

for x in tlist1:
	for y in tlist2:
		if x == y:
			cow += 1

cow = cow - bull

print("{0} bulls and {1} cows.".format(bull, cow))
