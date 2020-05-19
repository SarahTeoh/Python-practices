#課題6-2
from chiSquareTest import chi_square_test
from pi_stimulation import stimulate_pi
import statistics
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

accuracy = 0.01

def main():
	# Get user's input
	N = int(input("Please input N: "))
	M = int(input("M = "))

	mean_list = []
	N_list = []
	err_list = []

	while True:
		pi_list = []
		for i in range(M):
			#課題6-1の関数を使ってπの推定値を求める
			pi = stimulate_pi(N)
			pi_list.append(pi)
		
		mean = statistics.mean(pi_list)
		stdev = statistics.stdev(pi_list)

		#課題5-2の関数を使う
		chi, _, critical_value, _, _ = chi_square_test(pi_list)

		left, right = norm.interval(alpha=0.95, loc=mean, scale=stdev)

		if (chi < critical_value):
			if left > (mean - accuracy) and right < (mean + accuracy):
 				break
			else:
				mean_list.append(left+(right-left)/2)
				err_list.append((right-left)/2)
				N *= 2
				N_list.append(N)


	true_pi = [math.pi for x in range(len(N_list))]
	plt.errorbar(x = N_list, y =mean_list, yerr = err_list)
	plt.plot(N_list, true_pi, color="red", marker='o', markersize=4)
	plt.xscale('log')
	plt.xlabel("Num of Points")
	plt.ylabel("Confidence Interval")
	plt.show()

if __name__ == '__main__':
	main()