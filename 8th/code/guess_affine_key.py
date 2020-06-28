#課題11-8
import percentageOfWords
import sys
sys.path.append('../../7th/source/')
sys.path.append('../../6th/source/')
sys.path.append('../data/')
import euclidean_algorithm
import affine_cipher_decryption


LETTERS = affine_cipher_decryption.LETTERS
N = affine_cipher_decryption.N
# Maximum percentage of english words to determine whether to break loop
max_rate = 50

def main():
	file = input("Please input the path to textfile: ")
	# Initialize Break flag
	breakFlag = 0
	
	with open(file, "r") as f:
		encrypted = f.read()
		
		# Try every possible key
		for a in range(2, N):
			# If flag is raised means key found
			if breakFlag:
				break
			# 'a' must be relatively prime to N
			if euclidean_algorithm.find_gcd(a, N) != 1:
				continue
			for b in range(1, N):
				print("a, b = %d %d" % (a, b))
				decrypted = affine_cipher_decryption.decrypt(encrypted, a, b)
				rate = percentageOfWords.countWords(decrypted)
				print("rate = ", rate)
				# If percentage of english words over maximum percentage, means key found, break the loop
				if rate > max_rate:
					print("Key Found: %d %d" % (a, b))
					breakFlag = 1
					break

if __name__ == '__main__':
	main()