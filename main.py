#Simple linear regression using python from scratch
from csv import reader, writer
from math import sqrt
from os import getcwd

path = getcwd()

def mean(values):
	return sum(values) / float(len(values))
	
def covariance(x, mean_x, y, mean_y):
	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - mean_x) * (y[i] - mean_y)
	return covar

def variance(list, mean):
	return sum([(x - mean)**2 for x in list])

def coefficient(covar, var, mean_x, mean_y):
	b1 = covar / var
	b0 = mean_y - (b1 * mean_x)
	return b1, b0

def load_csv(dataset):
	init = 0
	x = list()
	y = list()
	with open(dataset) as file:
		content = reader(file)
		for row in content:
			if init == 0:
				init = 1
			else:
				x.append(row[0])
				y.append(row[1])
	return x, y
			
def split_dataset(x, y):
	train_x = list()
	train_y = list()
	test_x = list()
	test_y = list()
	training_size = int(.8 * len(x))
	train_x, test_x = x[0:training_size], x[training_size::]
	train_y, test_y = y[0:training_size], y[training_size::]
	return train_x, train_y, test_x, test_y

def predict(b0, b1, test_x):
	predicted_y = list()
	for i in test_x:
		predicted_y.append(b0 + b1 * i)
	return predicted_y
	
def rmse(predicted_y, test_y):
	error = 0.0
	for i in range(len(predicted_y)):
		sum_error = (predicted_y[i] - test_y[i]) ** 2
	return sqrt(sum_error / float(len(test_y)))
		
def main():
	try:
		dataset = path + "/Datasets/height_weight.csv"
		x, y = load_csv(dataset)
		#print(x,y)	
		x = [float(i) for i in x]
		y = [float(i) for i in y]		
		mean_x = mean(x)
		mean_y = mean(y)
		covar = covariance(x, mean_x, y, mean_y)
		var = variance(x, mean_x)
		train_x, train_y, test_x, test_y = split_dataset(x, y)			
		b1, b0 = coefficient(covar, var, mean_x, mean_y)
		predicted_y = predict(b0, b1, test_x)
		root_mean = rmse(predicted_y, test_y)
		print("Linear regression from scratch using python\n\nDataset name : height_weight.csv\nDataset source : http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_Dinov_020108_HeightsWeights\nSource code : https://github.com/gowtham758550/Linear-Regression-From-Scratch\n")
		print("Root mean : {}\n".format(root_mean))
		new_x = int(input("Enter height to predict the height(inches) : "))
		new_y = b0 + b1 * new_x
		print("Predicted weight(Pounds) : {}".format(new_y))
		
	except Exception as a:
		print(a)
	
main()
	