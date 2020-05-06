import csv
import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt

def standardize(data):
	mean = statistics.mean(data)
	stdev = statistics.stdev(data)
	return [(i - mean) / stdev for i in data]

def main():
	#Read data from csv file
	data = pd.read_csv('weight-height.csv')

	#Read male's height and weight data
	m_height = data[data.Gender=='Male']['Height'].tolist()
	m_weight = data[data.Gender=='Male']['Weight'].tolist()

	#Read female's height and weight data
	f_height = data[data.Gender=='Female']['Height'].tolist()
	f_weight = data[data.Gender=='Female']['Weight'].tolist()

	#Bind two lists as tuple in list
	m_weight_height = list(zip(m_weight, m_height))
	f_weight_height = list(zip(f_weight, f_height))

	#Get user's input
	gender = input("Please input gender: ")
	n = int(input("Please input the desired data size: "))

	#Randomly choose N data to plot   
	if gender == "female":
		chosen_data = random.sample(f_weight_height, n)
		standardized_height = standardize(list(zip(*chosen_data))[0])
		standardized_weight = standardize(list(zip(*chosen_data))[1])
	elif gender == "male":
		chosen_data = random.sample(m_weight_height, n)
		standardized_height = standardize(list(zip(*chosen_data))[0])
		standardized_weight = standardize(list(zip(*chosen_data))[1])
	else:
		print("Please insert only female of male without a space")

	#Plot graph
	fig = plt.figure()
	fig.set_figheight(15)
	fig.set_figwidth(25)

	#Top left
	before_standardization_height = fig.add_subplot(2, 3, 1)
	if gender == "female":
		before_standardization_height.scatter(*zip(*chosen_data), c='green', alpha=0.3, label='Female')
	elif gender == "male":
		before_standardization_height.scatter(*zip(*chosen_data), c='green', alpha=0.3, label='Male')
	before_standardization_height.set_xlabel("Height")
	before_standardization_height.set_ylabel("Weight")
	before_standardization_height.legend()

	before_standardization_height = fig.add_subplot(2, 3, 2)
	before_standardization_height.hist(list(zip(*chosen_data))[0], color='red', alpha=0.5, label='Before Standarize Height')
	before_standardization_height.set_xlabel("Height")
	before_standardization_height.set_ylabel("Num of People")
	before_standardization_height.legend()

	#Top right
	before_standardization_weight = fig.add_subplot(2, 3, 3)
	before_standardization_weight.hist(list(zip(*chosen_data))[1], color='red', alpha=0.5, label='Before Standarize Weight')
	before_standardization_weight.set_xlabel("Weight")
	before_standardization_weight.set_ylabel("Num of People")
	before_standardization_weight.legend()

	#Bottom left
	after_standardization_height = fig.add_subplot(2, 3, 5)
	after_standardization_height.hist(standardized_height, color='blue', alpha=0.5, label='After Standarized Height')
	after_standardization_height.set_xlabel("Height")
	after_standardization_height.set_ylabel("Num of People")
	after_standardization_height.legend()

	#Bottom right
	after_standardization_weight = fig.add_subplot(2, 3, 6)
	after_standardization_weight.hist(standardized_weight, color='blue', alpha=0.5, label='After Standarized Weight')
	after_standardization_weight.set_xlabel("Weight")
	after_standardization_weight.set_ylabel("Num of People")
	after_standardization_weight.legend()
	
	fig.savefig('standardization.jpg')
	

if __name__ == '__main__':
	main()