#2分法
#main関数から入力とepsilonの値を引数として引き渡す
def bisection_method(a, epsilon):
	numGuesses = 0
	if a < 1:
		low = a
		high = 1.0

	else:
		low = 0.0
		high = a

	x = (high - low)/2.0
	while abs(x**2 - a) >= epsilon:
		if x**2 < a:
			low = x
		else:
			high = x
		x = (high + low)/2.0
		numGuesses += 1

	return x, numGuesses

#ニュートン法
#main関数から入力とepsilonの値を引数として引き渡す
def newton_method(a, epsilon):
	numGuesses = 0
	x = a

	while abs(x**2 - a) >= epsilon:
		x_new = x - (x * x - a) / (x * 2)
		x = x_new
		numGuesses += 1

	return x, numGuesses

def main():
	a = float(input("Please input a positive number: "))
	epsilon = 0.01
	ans, guess = bisection_method(a, epsilon)　#2分法の関数から返す二つの値をそれぞれansとguessに格納する
	if abs(ans**2 - a) >= epsilon:
		print("Failed on square root of ", a)
	else:
		print("The square root of ", a, "using Bisection method(2分法) ", "is ", ans)
		print("Number of guesses using Bisection method: ", guess, "\n")
		ans, guess = newton_method(a, epsilon)　#ansとguessの値をニュートン法の場合の結果に変更する
		print("The square root of ", a, "using Newton method(ニュートン法) ", "is ", ans)	
		print("Number of guesses using Newton method: ", guess, "\n")

#他のプログラムからインポートではなくこのプログラム自体が実行された時にmain関数を呼び出す
if __name__=="__main__":
	main()