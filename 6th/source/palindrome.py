#課題9

def main():
	path = '../data/'
	filename = 'english_wordlist.txt'
	
	palindrome_num = 0
	palindrome = []
	with open(path+filename) as f:
    	for string in f:
			if(string==string[::-1]):
				palindrome_num += 1
				palindrome.append(strinig)
			else:
			     continue

	print(palindrome)

if __name__ == '__main__':
	main()