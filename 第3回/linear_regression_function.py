#課題4-3
import csv
import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt

def standardize(data):
	mean = statistics.mean(data)
	stdev = statistics.stdev(data)
	return [(i - mean) / stdev for i in data]

def calc_mse(height_array, weight_array, a, b):
	square_error = [(weight_array[height_array.index(height)]-(a * height + b))**2 for height in height_array]
	mse = sum(square_error)/len(height_array)
	return mse

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
	n = int(input("Please input N: "))
	a = int(input("Please input a: "))
	b = int(input("Please input b: "))

	#Randomly choose N data to plot   
	if gender == "female":
		chosen_data = random.sample(f_weight_height, n)
	elif gender == "male":
		chosen_data = random.sample(m_weight_height, n)
	else:
		print("Please insert only female of male")

	standardized_height = standardize(list(zip(*chosen_data))[0])
	standardized_weight = standardize(list(zip(*chosen_data))[1])

	print(calc_mse(standardized_height, standardized_weight, a, b))
	
if __name__ == '__main__':
	main()