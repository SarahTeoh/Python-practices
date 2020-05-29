#課題7-4
import csv
import pandas as pd
import random
import numpy as np
import math
from scipy.stats import norm

n = 1200
repetition = 10000

def main():
	data = pd.read_csv('../../csv/marathon_results.csv')
	time =  data['time'].tolist() 
	population_mean = np.mean(time)
	population_std = np.std(time)
	#sample_std = population_std/math.sqrt(n)

	out_of_range = 0

	for i in range(repetition):
		randomly_selected_time = random.sample(time, n) 
		sample_mean = np.mean(randomly_selected_time)
		sample_std = np.std(randomly_selected_time)/math.sqrt(n)
		
		left, right = norm.interval(alpha=0.95, loc=sample_mean, scale=sample_std)

		if not left < population_mean < right:
			out_of_range += 1

	print("n=", n)
	print("全選手の平均タイムが求めた信頼区間に入らない割合:", out_of_range*100/repetition, "%")

if __name__ == '__main__':
	main()