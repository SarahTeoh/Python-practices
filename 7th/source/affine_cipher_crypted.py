#課題11-4
from find_affine_key import generate_keys
from affine_cipher import encrypt

with open("plaintext.txt", "r") as f_in:
	with open("crypted.txt", "w") as f_out:
		message = f_in.read()
		a, b = generate_keys()
		f_out.write(encrypt(message, a, b))