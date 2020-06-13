#課題11-2
import random
from euclidean_algorithm import find_gcd
import sys
sys.path.append('../../6th/source/')
import caeser_cipher

LETTERS = caeser_cipher.LETTERS
N = len(LETTERS)

def generate_keys(N):
	keyB = random.randint(1, N)
	keyA = random.randint(2, N)
	while find_gcd(keyA, N) != 1:
		keyA = random.randint(2, N)
	
	return keyA, keyB

def main():
	a, b = generate_keys(N)
	print("keyA: %d, keyB: %d"%(a, b))

if __name__=="__main__":
	main()