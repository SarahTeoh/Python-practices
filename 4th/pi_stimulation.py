#課題6-1
import random
import numpy as np

def stimulate_pi(N):
	data = np.random.rand(N, 2)
	
	P = 0
	for coordinates in data:
		if ((coordinates[0]**2 + coordinates[1]**2) <= 1):
			P += 1

	pi = 4*P/N
	return pi

def main():
	# Get user's input
	N = int(input("Please input N: "))

	pi = stimulate_pi(N)
	print("πの推定値: ", pi)

if __name__ == '__main__':
	main()