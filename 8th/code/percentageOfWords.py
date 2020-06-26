#課題11-7
import re

with open("../data/english_wordlist.txt", "r") as f_eng_words:
	eng_words = f_eng_words.read().split('\n')

def main():
	file = input("Please input the path to textfile: ")
	total_count = 0
	eng_count = 0
	alphabet_only_words = []

	with open(file, "r") as f:
		for line in f:
			line = line.replace('\n', '')
			words_list = line.split(" ")
			total_count += len(words_list)
			words = re.findall(r"[A-Za-z]+", line)
			for word in words:
				if word in eng_words:
					alphabet_only_words.append(word)
					eng_count += 1

	print("Total words found: ", total_count)
	print("Total english words found: ", eng_count)
	percentage = (eng_count*100/total_count)
	print("%f %% English Words" %percentage)

	print("words found:", alphabet_only_words)

if __name__ == '__main__':
	main()