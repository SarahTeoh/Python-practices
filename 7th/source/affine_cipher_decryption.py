#課題11-6
import affine_cipher_crypted 
from extended_euclidean_algorithm import modinv
import sys
sys.path.append('../../6th/source/')
import caeser_cipher 

LETTERS = caeser_cipher.LETTERS
N = len(LETTERS)

# Affine cipher decoder
def decrypt(message, keyA, keyB):
	# Initialize decrypted message
	decrypted = ""
	# For every character in the message
	# find index of the character from LETTERS
	# inverse the shift of the index with key
	for char in message:
		i = LETTERS.find(char)
		j = (modinv(keyA, N)*(i - keyB)) % N
		decrypted += LETTERS[j]

	return decrypted

def main():
	with open("crypted.txt", "r") as f_in:
		with open("decrypted.txt", "w") as f_out:
			encrypted = f_in.read()
			f_out.write(decrypt(encrypted, affine_cipher_crypted.a, affine_cipher_crypted.b))

if __name__=="__main__":
	main()
