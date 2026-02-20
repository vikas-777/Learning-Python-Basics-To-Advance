def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
print(gcd(69,42))

def x_gcd(a,b):
    if b==0:
        return a
    elif a == 0:
        return b
    else:
        return x_gcd(b,a%b)
print(x_gcd(0,55))

n1 = int(input("Enter the number 1."))

n2 = int(input("Enter the number 2."))
while n2!=0:
    n1,n2=n2,n1%n2
print(f"gcd is {n1}")