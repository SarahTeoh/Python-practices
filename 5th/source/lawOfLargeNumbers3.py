#課題7-3
import csv
import pandas as pd
import random
import numpy as np
import math
import matplotlib.pyplot as plt

L = 100

def main():
	data = pd.read_csv('../../csv/marathon_results.csv')
	time =  data['time'].tolist() 
	population_std = np.std(time)
	
	N_list = [i for i in range(5, 1010, 30)] # List of N (x-axis of graph)
	average_difference = []

	for n in N_list:
		difference = []
		for i in range(L):
			randomly_selected_time = random.sample(time, n) 
			sample_std = np.std(randomly_selected_time)
			difference.append(abs(sample_std - population_std))

		average_difference.append(np.mean(difference))

	plt.plot(N_list, average_difference, color="red")
	plt.xlabel("Sample Size N")
	plt.ylabel("Diff between Population Std and Sample Std")
	plt.show()

if __name__ == '__main__':
	main()