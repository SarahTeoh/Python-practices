#課題7-2
import csv
import pandas as pd
import random
import numpy as np
import math
import matplotlib.pyplot as plt

m = 1000

def main():
	data = pd.read_csv('../../csv/marathon_results.csv')
	time =  data['time'].tolist() 
	stdev_of_all_data = np.std(time)
	
	N_list = [i for i in range(100, 3000, 200)] # List of N (x-axis of graph)
	standard_error_list = [] 
	stdev_list = []

	for n in N_list:
		standard_error_list.append(stdev_of_all_data/math.sqrt(n))
		sample_mean = [] 
		for i in range(m):
			randomly_selected_time = random.sample(time, n) 
			sample_mean.append(np.mean(randomly_selected_time))

		stdev_list.append(np.std(sample_mean))

	plt.plot(N_list, standard_error_list, color="blue", marker='o', markersize=4, label="Standard Error")
	plt.plot(N_list, stdev_list, color="red", marker='x', markersize=4, label="Std of %d samples"%m)
	plt.legend(loc="upper right")
	plt.xlabel("Sample Size N")
	plt.ylabel("Standard Deviation")
	plt.show()

if __name__ == '__main__':
	main()