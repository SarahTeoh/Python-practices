#課題8
import matplotlib.pyplot as plt
import random
from itertools import permutations

def main():
	n = int(input("Please input how many cards(N):")) # Total number of cards

	a = list(range(1, n+1))
	all_permutations = list(permutations(a)) # List out all possible permutations
	win_rate_list = [] # List to record probability of winning of every m

	for m in range(1, n):
		times_of_winning = 0
		for permutation in all_permutations:
			# Wins if [maximum value(N) exists after Mth card] and [no value bigger than maximum of M between M-Nth card]
			if (permutation.index(n) >= m) and (max(permutation[:m]) == max(permutation[:permutation.index(n)])):
				times_of_winning += 1
				continue
			else:
				continue

		win_rate_list.append(times_of_winning/len(all_permutations))

	plt.plot(range(1, n), win_rate_list)
	plt.xlabel("M")
	plt.ylabel("Win rate")
	plt.show()

if __name__ == '__main__':
	main()