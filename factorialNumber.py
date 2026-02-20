n = int(input("Enter number..."))
fact = 1
number = n
if n == 0:
    print(f"Factorial of {number} = {fact}")
elif n < 0:
    print("Factorial works on positive numbers")
else:
    while n >= 1:
        fact = fact * n
        n -= 1
    print(f"Factorial of {number} = {fact}")
###################################################################################
for i in range(n,1,-1):
    fact = fact * n
    n = n-1
print(fact)