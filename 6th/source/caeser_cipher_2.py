#課題10-2
from caeser_cipher import decrypt, N

if __name__=="__main__":
	with open("../data/enc_wc.txt", "r") as f:
		first_few_lines_list = [f.readline() for i in range(3)] # Read first 3 lines
		first_few_lines = "".join(first_few_lines_list) # Join the first 3 lines

		# Loop through all possible keys between 1 and N 
		for key in range(1, N):
			# Try to decrypt the first few lines with ket
			decrypted = decrypt(first_few_lines , key)
			print("Key: ", key)
			# Print out the decrypted first few lines to check whether key used is valid
			print("Decrypted first few lines:", decrypted, "\n")
			# Choose to try another possible key if the key was wrong, continue to decrypt whole passage if correct key
			continue_annot = int(input("Please input 0 to continue to try the next possible key, 1 to decrypt whole passage: "))
			# If correct key
			if continue_annot:
				print("Key Found: ", key)
				break
			# If wrong key then continue to try next possible key
			else:
				continue

		# Read the whole passage, decrypt and print out
		leftover_lines = f.read().rstrip("\n")
		decrypted_leftover = decrypt(leftover_lines, key)
		decrypted += decrypted_leftover
		print("Original text: ")
		print(decrypted)

		
