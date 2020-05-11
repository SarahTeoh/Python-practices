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

def renew_paramaters(height_array, weight_array, initial_a, initial_b, learning_rate):
	w = (np.array([initial_a, initial_b])).T  
	X = np.array([(np.array([height, 1])).T for height in height_array]) 
	y = (np.array([weight for weight in weight_array])).T 
	df = (np.dot(X.T, (np.dot(X, w) - y)))/len(height_array)
	w = w - learning_rate * df
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
	m_weight_height = list(zip(m_weight, m_height))
	f_weight_height = list(zip(f_weight, f_height))

	#Get user's input
	gender = input("Please input gender: ")
	n = int(input("Please input N: "))
	a = int(input("Please input a: "))
	b = int(input("Please input b: "))
	learning_rate = float(input("Please input learning rate: "))
	max_range = int(input("Please input maximum iteration number: "))

	#Randomly choose N data to plot   
	if gender == "female":
		chosen_data = random.sample(f_weight_height, n)
	elif gender == "male":
		chosen_data = random.sample(m_weight_height, n)
	else:
		print("Please insert only female of male")

	standardized_height = standardize(list(zip(*chosen_data))[0])
	standardized_weight = standardize(list(zip(*chosen_data))[1])

	mse = calc_mse(standardized_height, standardized_weight, a, b)
	final_a = a
	final_b = b
	updated_mse = []
	new_ab = np.array([a, b])
	
	for i in range(0, max_range , 1):
		new_ab = renew_paramaters(standardized_height, standardized_weight, new_ab[0], new_ab[1], learning_rate)
		new_mse = calc_mse(standardized_height, standardized_weight, new_ab[0], new_ab[1])
		updated_mse.append(new_mse)
		if new_mse <= mse:
			mse = new_mse
			final_a = new_ab[0]
			final_b = new_ab[1]

	estimated_weight = [final_a * height + final_b for height in standardized_height]

	print("min mse: ", mse)
	print("a: ", final_a)
	print("b: ", final_b)

	#Plot graph
	fig = plt.figure()
	fig.set_figheight(15)
	fig.set_figwidth(25)
	
	#Left
	graph = fig.add_subplot(1, 2, 1)
	graph.plot(np.arange(0, max_range, 1), np.array(updated_mse), color='red', alpha=0.5)
	graph.set_xlabel("Iteration")
	graph.set_ylabel("MSE")

	#Right
	graph = fig.add_subplot(1, 2, 2)
	graph.scatter(standardized_height, standardized_weight, color='red', alpha=0.5, label='data')
	graph.plot(np.array(standardized_height), np.array(estimated_weight), color='blue', alpha=0.5, label='y=ax+b')
	graph.set_xlabel("Height")
	graph.set_ylabel("Weight")
	graph.legend()

	fig.savefig('graph.jpg')

if __name__ == '__main__':
	main()