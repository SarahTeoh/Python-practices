import random
import matplotlib.pyplot as plt
from scipy.stats import chi2
from scipy.stats import norm
import numpy as np
from collections import Counter
import math

M = 5000 #Repetition times
N = 5000 #Number of data
k = int(1 + math.log2(N))
kai_list = []

for i in range(M):
	num_list = np.random.randn(N) #N個の乱数生成
	bins = k
	freq, max_of_bins = np.histogram(num_list, bins=k) # ヒストグラムを作成
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
	kai_list.append(kai)

bins = range(50)
plt.hist(kai_list, bins=bins, density=True, label="χ^2分布") # ヒストグラムを描画
plt.plot(bins, chi2.pdf(bins, k-1), label="自由度k-1のχ^2分布") # カイ2乗分布（自由度N-1）を描画
plt.savefig("kadai51.png")
