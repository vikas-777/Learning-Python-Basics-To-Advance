# sum of n natural numbers
n = int(input("Enter the number: "))
sum = 0
for i in range(n + 1):
    sum += i
print(f"sum of {n} numbers = {sum}")
