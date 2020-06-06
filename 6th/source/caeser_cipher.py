#課題10-1
import random

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOLS = " -!\"&\'()*,.:;[]_`?\n"
NUMBERS = '0123456789'
LETTERS = UPPER+LOWER+NUMBERS+SYMBOLS
N = len(LETTERS)

# Check whether unknown characters inserted
def check(message):
	diff = set(message) - set(LETTERS)
	if diff:
		return 0, diff
	else:
		return 1, diff

# Caeser cipher encoder
def encrypt(message, shift):
	# Initialize encrypted message
	encrypted = "" 
	# For every character in the message
	# find index of the character from LETTERS
	# shift the index with the key
	for char in message:
		i = LETTERS.find(char)
		j = (i + shift) % N
		encrypted += LETTERS[j]

	return encrypted

# Caeser cipher decoder
def decrypt(message, shift):
	# Initialize decrypted message
	decrypted = ""
	# For every character in the message
	# find index of the character from LETTERS
	# inverse the shift of the index with key
	for char in message:
		i = LETTERS.find(char)
		j = (i - shift) % N
		decrypted += LETTERS[j]

	return decrypted

if __name__=="__main__":
	message = input("Please insert message: ")
	valid, diff = check(message) # Check for unknown characters
	# If no unknown characters
	if valid:
		shift = random.randint(1, N) # Generate key where 1 <= key <= N
		print("shift:", shift)
		encrypted = encrypt(message, shift)
		print("encrypted message: ", encrypted)
		decrypted = decrypt(encrypted, shift)
		print("decrypted message: ", decrypted)
	# If unknown characters exist
	else:
		print("your message contains illegal letters: ", ', '.join(diff))
