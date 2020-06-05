#課題7-2
import math
import matplotlib.pyplot as plt
import lawOfLargeNumbers1

# Repetition times
m = 1000

def main():
	# Get population standard deviation, mean of sample mean, standard deviation of sample mean from another program
	population_stdev, sample_mean_mean_to_plot, sample_mean_stdev_to_plot = lawOfLargeNumbers1.main()

	# X-axis of graph
	N_list = list(range(100, 3000, 200))

	# Standard error list
	standard_error_list = [population_stdev/math.sqrt(n) for n in N_list]
	
	# Plot graph
	plt.plot(N_list, standard_error_list, color="blue", marker='o', markersize=4, label="Standard Error")
	plt.plot(N_list, sample_mean_stdev_to_plot, color="red", marker='x', markersize=4, label="Std of %d samples"%m)
	plt.legend(loc="upper right")
	plt.xlabel("Sample Size N")
	plt.ylabel("Standard Deviation")
	plt.show()

if __name__ == '__main__':
	main()