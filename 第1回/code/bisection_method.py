a = float(input("Please input a positive number: "))

epsilon = 0.01
numGuesses = 0

#1より小さい、大きいの2つに場合分け
if a < 1:
	#1より小さい場合
	#入力を解が存在する区間の左側に，1を右側にする
	low = a
	high = 1.0

else:
	#1より大きい場合
	#0を解が存在する区間の左側に，入力を右側にする
	low = 0.0
	high = a

#真ん中の値を計算する
x = (high - low)/2.0

#x**2とaの誤差がepsilon未満となるxを探索
while abs(x**2 - a) >= epsilon:
	#真ん中の値xの2乗が入力より小さければxを左側にそうでなければ右側に
	if x**2 < a:
		low = x
	else:
		high = x
	#新しい解区間の真ん中の値を計算
	x = (high + low)/2.0
	numGuesses += 1

print("numGuesses = ", numGuesses)
if abs(x**2 - a) >= epsilon:
	print("Failed on square root of ", a)
else:
	print(x, " is close to square root of ", a)
