#課題11-5

# Extended Euclidean Algorithm for finding modular inverse 
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


def main():
    #ユーザからa,bを入力
    a = int(input("a: "))
    b = int(input("b: "))

    #a,bを関数に入れてgcdが帰ってくる
    gcd, x, y  = egcd(a, b)
    print("gcd:", gcd)
    print("x:", x)
    print("y:", y)

if __name__ == '__main__':
    main()

