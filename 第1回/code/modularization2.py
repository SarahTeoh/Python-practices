#作ったプログラムをモジュールとしてインポート
import modularization

def main():
	a = float(input("Please input a positive number: "))
	epsilon = 0.01
	ans, guess = modularization.bisection_method(a, epsilon) #インポートしたモジュールの中のbisection_method関数を呼び出す
	if abs(ans**2 - a) >= epsilon:
		print("Failed on square root of ", a)
	else:
		print("The square root of ", a, "using Bisection method(2分法) ", "is ", ans)
		print("Number of guesses using Bisection method: ", guess, "\n")
		ans, guess = modularization.newton_method(a, epsilon) #インポートしたモジュールの中のnewton_method関数を呼び出す
		print("The square root of ", a, "using Newton method(ニュートン法) ", "is ", ans)	
		print("Number of guesses using Newton method: ", guess, "\n")

if __name__ == '__main__':
	main()