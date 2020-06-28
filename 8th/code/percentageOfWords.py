#課題11-7
import re

def countWords(text):
	# Store all english words in a eng_words list
	with open("../data/english_wordlist.txt", "r") as f_eng_words:
		eng_words = f_eng_words.read().split('\n')

	# Initialize all variables to store total number of words,
	#number of english words 
	#and english words 
	total_count = 0
	eng_count = 0
	eng_words_found = []

	# Replace all non-alphabetic characters with a space
	words = re.sub('[^a-zA-Z]+', ' ', text)

	# Split into list using space as separator
	words_list = words.split(" ")
	# Total number of words
	total_count += len(words_list)
	
	# Check for english words in the list
	for word in words_list:
		if word in eng_words:
			eng_count += 1
			eng_words_found.append(word)

	# Calculate percentage of English words
	percentage = (eng_count*100/total_count)

	print("eng_words_found: ", eng_words_found)
	print("English Words Found: %d" % eng_count)
	print("Total Words Found: %d" % total_count)
	return percentage
