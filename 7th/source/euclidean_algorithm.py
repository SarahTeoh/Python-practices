#課題11-1

def find_gcd(x, y):
	if x == 0 : 
		return y
	return find_gcd(y%x, x)

def main():
	x = int(input("Please input x:"))
	y = int(input("Please input y:"))
	
	gcd = find_gcd(x, y)
	print("GCD(%d, %d): %d"%(x, y, gcd))

if __name__ == '__main__':
	main()