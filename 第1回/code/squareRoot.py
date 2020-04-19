a = float(input("Please input a positive number: "))　#int()をfloat()に、"positive integer"を"positive number"に変更

x = 0.0
epsilon = 0.01
step = epsilon**2
numGuesses = 0

#1より小さい、大きいの2つに場合分け
if a < 1:
	while abs(x**2-a) >= epsilon:
	    x += step
	    numGuesses += 1
else:
	while abs(x**2-a) >= epsilon and x < a:
	    x += step
	    numGuesses += 1

print("numGuesses = ", numGuesses)
if abs(x**2 - a) >= epsilon:
    print("Failed on square root of ", a)
else:
    print(x, " is close to square root of ", a)



