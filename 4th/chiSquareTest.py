#課題5-2
import csv
import pandas as pd
import numpy as np
from scipy.stats import chisquare
from scipy.stats import chi2
import math
from standardization import standardize # Import function from standardization.py
from kaiSquare import calc_chi # Import function from kaiSquare.py

def chi_square_test(data):
	N = len(data)
	k = int(1 + math.log2(N)) #Sturges' formula

	standardized_data = standardize(data)
	standardized_data_array = np.array(standardized_data)

	# Calculate chi
	chi, freq, expected_freq = calc_chi(standardized_data_array)

	# Calculate critical value for 95% confidence
	critical_value = chi2.ppf(q = 0.95, df = k-1) 
                      
    # Find the p-value
	p_value = 1 - chi2.cdf(x = chi, df = k-1) 

	return chi, p_value, critical_value, freq, expected_freq

def main():
	# Read data from csv file
	#data = pd.read_csv('weight-height.csv')
	data = pd.read_csv('marathon_results.csv')

	# Read male's height data
	#m_height = data[data.Gender=='Male']['Height'].tolist()
	#m_weight = data[data.Gender=='Male']['Weight'].tolist()
	#f_height = data[data.Gender=='Female']['Height'].tolist()
	#f_weight = data[data.Gender=='Female']['Weight'].tolist()
	#m_time =  data[data.gender=='M']['time'].tolist()
	f_time =  data[data.gender=='F']['time'].tolist()

	#chi, p_value, critical_value = chi_square_test(m_height)
	#chi, p_value, critical_value = chi_square_test(f_weight)
	#chi, p_value, critical_value = chi_square_test(m_height)
	#chi, p_value, critical_value = chi_square_test(f_weight)
	#chi, p_value, critical_value = chi_square_test(m_time)
	chi, p_value, critical_value, freq, expected_freq = chi_square_test(f_time)

	# Prints out results and conclusion
	print("カイ2乗値: ", chi)
	print("p値: ", p_value)
	print("棄却域: ", critical_value)

	if(chi < critical_value):
		print("結論: 帰無仮説を採択する．観測データは正規分布に従う.\n")
	else:
		print("結論: 対立仮説を採択する．観測データは正規分布に従わない.\n")

	# Check result using scipy.stats function
	print("scipy.statsのchisquare関数を使った検算: ")
	print(chisquare(f_obs= freq, f_exp= expected_freq))

	
if __name__ == '__main__':
	main()