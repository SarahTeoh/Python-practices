#課題11-3
from find_affine_key import generate_keys
import sys
sys.path.append('../../6th/source/')
import caeser_cipher 

LETTERS = caeser_cipher.LETTERS
N = len(LETTERS)

# Affine cipher encoder
def encrypt(message, keyA, keyB):
	# Initialize encrypted message
	encrypted = "" 

	# For every character in the message
	# find index of the character from LETTERS
	# shift the index with the key
	for char in message:
		i = LETTERS.find(char)
		j = (keyA*i + keyB) % N
		encrypted += LETTERS[j]

	return encrypted

# Extended Euclidean Algorithm for finding modular inverse 
# eg: modinv(7, 26) = 15 
def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 

def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m 

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
	message = input("Please insert message: ")
	valid, diff = caeser_cipher.check(message) # Check for unknown characters
	# If no unknown characters
	if valid:
		keyA, keyB = generate_keys()
		encrypted = encrypt(message, keyA, keyB)
		print("keyA: %d, keyB: %d"%(keyA, keyB))
		print("encrypted message: ", encrypted)
		decrypted = decrypt(encrypted, keyA, keyB)
		print("decrypted message: ", decrypted)
	# If unknown characters exist
	else:
		print("your message contains illegal letters: ", ', '.join(diff))

if __name__=="__main__":
	main()
