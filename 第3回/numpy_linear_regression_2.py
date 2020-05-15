#課題4-6
import csv
import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline

def standardize(data):
	mean = statistics.mean(data)
	stdev = statistics.stdev(data)
	return [(i - mean) / stdev for i in data]

def calc_mse(height_array, weight_array, a, b):
	square_error = [(weight_array[height_array.index(height)]-(a * height + b))**2 for height in height_array]
	mse = sum(square_error)/(2*len(height_array))
	return mse

def find_min_w_solution(height_array, weight_array):
	X = np.array([(np.array([height, 1])).T for height in height_array]) 
	y = (np.array([weight for weight in weight_array])).T 
	w = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))
	return w
	

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
	m_weight_height = list(zip(m_height, m_weight))
	f_weight_height = list(zip(f_height, f_weight))

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

	final_w = find_min_w_solution(standardized_height, standardized_weight)
	min_mse = calc_mse(standardized_height, standardized_weight, final_w[0], final_w[1])
	estimated_weight = [final_w[0] * height+ final_w[1] for height in standardized_height]

	print("min mse: ", min_mse)
	print("a: ", final_w[0])
	print("b: ", final_w[1])

	#Plot graph
	plt.scatter(standardized_height, standardized_weight, color='red', alpha=0.5, label='data')
	plt.plot(np.array(standardized_height), np.array(estimated_weight), color='blue', alpha=0.5, label='y=ax+b')
	plt.xlabel("Height")
	plt.ylabel("Weight")
	plt.legend()

	plt.savefig('kinjichokusen.jpg')

if __name__ == '__main__':
	main()