#課題9

def main():
	path = '../data/'
	filename = 'english_wordlist.txt'
	
	palindrome_num = 0
	palindrome = []
	with open(path+filename, 'r') as f:
		texts = [line.rstrip('\n') for line in f]
		
	for word in texts:
		# word[::-1] is reversed word
		if(word==word[::-1]):
			palindrome_num += 1
			palindrome.append(word)
		else:
		     continue

	print("Total palindrome: ", palindrome_num)
	print(palindrome)

if __name__ == '__main__':
	main()