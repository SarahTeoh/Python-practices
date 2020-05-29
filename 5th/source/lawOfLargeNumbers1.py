#課題7-1
import csv
import pandas as pd
import random
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import sys
sys.path.append("../4th")
from chiSquareTest import chi_square_test

m = 1000
"""
def calc_mean(List):
	return sum(List)/len(List)
"""
def main():
	data = pd.read_csv('../csv/marathon_results.csv')
	time =  data['time'].tolist() 
	mean_of_all_data = np.mean(time)

	
	sample_mean_to_plot = [] # List of mean of sample that are normal distributed (y-axis of graph)
	N_list = [] # List of N of sample that are normal distributed (x-axis of graph)
	err_list = [] # List of range that contains 95 percent of the distribution
	n = 100 # Initial value of N

	while n < 2800:
		sample_mean = [] 
		for i in range(m):
			randomly_selected_time = random.sample(time, n) 
			sample_mean.append(np.mean(randomly_selected_time))

		sample_mean_mean = np.mean(sample_mean)
		sample_mean_stdev = np.std(sample_mean)
		print("N=%dの標本平均の平均:%f"%(n, sample_mean_mean))
		print("N=%dの標本平均の標準偏差:%f"%(n, sample_mean_stdev))

		chi, _, critical_value, _, _ = chi_square_test(sample_mean)

		# Prints out results and conclusion
		print("カイ2乗値: ", chi)
		print("棄却域: ", critical_value)

		if(chi < critical_value):
			print("N=%dの標本平均は正規分布に従う.\n"%n)
			N_list.append(n)
			sample_mean_to_plot.append(sample_mean_mean)
			left, right = norm.interval(alpha=0.95, loc=sample_mean_mean, scale=sample_mean_stdev)
			err_list.append((right-left)/2)
		else:
			print("N=%dの標本平均は正規分布に従わない.\n"%n)

		n += 200

	true_mean = [mean_of_all_data for x in range(len(N_list))]
	plt.errorbar(x = N_list, y =sample_mean_to_plot, yerr = err_list, label="Sample Mean and 95% Confidence Interval")
	plt.plot(N_list, true_mean, color="red", marker='o', markersize=4, label="Population Mean")
	plt.legend(loc="upper right")
	plt.xlabel("Sample Size N")
	plt.ylabel("Time")
	plt.show()

if __name__ == '__main__':
	main()