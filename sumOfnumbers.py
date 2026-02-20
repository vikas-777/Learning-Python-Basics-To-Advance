# sum of n natural numbers
n = int(input("Enter the number: "))
sum = 0
for i in range(n + 1):
    sum = sum + i
print(f"sum of {n} numbers = {sum}")
total = 0
i = 1
while i <= n:
    total = total +i
    i = i +1
print(f"sum of {n} numbers = {total}")
