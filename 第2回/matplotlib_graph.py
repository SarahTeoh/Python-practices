import csv
import pandas as pd
import random
import matplotlib.pyplot as plt

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
		#Use * to unzip chosen tuple into height and weight list 
		plt.scatter(*zip(*chosen_data), c='red', alpha=0.3, label='Female')
	elif gender == "male":
		chosen_data = random.sample(m_weight_height, n)
		plt.scatter(*zip(*chosen_data), c='blue', alpha=0.3, label='Male')
	else:
		print("Please insert only female of male")

	#Label axes and save graph
	plt.xlabel("Height")
	plt.ylabel("Weight")
	plt.savefig('height-weight.jpg')

if __name__ == '__main__':
	main()