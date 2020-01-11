# Justin Ventura
# 01/11/20
# linearreg.py
# Gull Code 2019

x = []
y = []

with open('dataset_275139_1.txt', 'r') as fp:
	line = fp.readline()
	print(line)
	observations = 1
	while line:
		x = list(line.split(' '))

print(x)