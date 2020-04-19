a = float(input("Please input a positive number: "))

epsilon = 0.01
numGuesses = 0
x = a

while abs(x**2 - a) >= epsilon:
	#ニュートン法の式
	x_new = x - (x * x - a) / (x * 2)
	x = x_new
	numGuesses += 1

print("numGuesses = ", numGuesses)
if abs(x**2 - a) >= epsilon:
	print("Failed on square root of ", a)
else:
	print(x, " is close to square root of ", a)
