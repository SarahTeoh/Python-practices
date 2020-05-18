#課題5-1
import random
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import numpy as np
import math

def calc_chi(data_array):
	N = data_array.size
	k = int(1 + math.log2(N)) #Sturges' formula
	freq, max_of_bins = np.histogram(data_array, bins=k) #Make histogram
	expected_freq = [0]*len(freq)
	kai =0
	
	for i in range(len(freq)):
		if i == 0:
			expected_freq[i] = norm.cdf(max_of_bins[i+1], 0, 1)*N
		elif i == len(freq)-1 :
			expected_freq[i] = (1 - norm.cdf(max_of_bins[i], 0, 1))*N
		else:
			expected_freq[i] = (norm.cdf(max_of_bins[i+1], 0, 1) - norm.cdf(max_of_bins[i], 0, 1))*N
		
	kai = [((f-e)**2)/e for f, e in zip(freq, expected_freq)]
	kai = sum(kai)
	return kai


def main():
	#Get user's input
	N = int(input("Please input total number of data: "))
	M = int(input("Please input the repetition time: "))
	
	chi_list = []

	for i in range(M):
		num_list = np.random.randn(N) #Generate N random numbers
		chi = calc_chi(num_list)
		chi_list.append(chi)

	bins = range(50)
	k = int(1 + math.log2(N)) #Sturges' formula
	plt.hist(chi_list, bins=bins, density=True, label="χ^2分布") #Plot histogram
	plt.plot(bins, chi2.pdf(bins, k-1), label="自由度k-1のχ^2分布") #Plot chi-squrare distribution (degrees of freedom N-1)
	plt.savefig("kadai51.png")


if __name__ == '__main__':
	main()