# Justin Ventura
# 01/11/20
# linearreg.py
# Gull Code 2019

# Empty datasets (x = Iv, y = Dv)
import matplotlib.pyplot as plt
x = []
y = []

def mean(data):
	return (float(sum(data)) / float(len(data)))

def variance(data, mean):
	return sum([(k - mean) ** 2 for k in data])

def covariance(x_data, x_mean, y_data, y_mean):
	covar = 0.0
	for i in range(len(x_data)):
		covar += (x_data[i] - x_mean) * (y_data[i] - y_mean)
	return covar

def coefficients(x_data, y_data):
	x_mean, y_mean = mean(x_data), mean(y_data)
	b1 = covariance(x_data, x_mean, y_data, y_mean) / variance(x_data, x_mean)
	b0 = y_mean - b1 * x_mean
	return [b0, b1]

with open('dataset_275139_1.txt', 'r') as fp:
	line = fp.readline()
	observations = 0
	while line:
		x0, y0 = line.strip().split()
		x.append(float(x0))
		y.append(float(y0))
		line = fp.readline()
		observations += 1

b0, b1 = coefficients(x, y)
print('based on {0} observations...'.format(observations))
print('intercept of linear model: ', b0)
print('slope of the linear model: ', b1)

def premodel(x_data):
	return b1 * x_data + b0

regression_model = list(map(premodel, x))

plt.scatter(x, y)
plt.plot(x, regression_model)
plt.show()

