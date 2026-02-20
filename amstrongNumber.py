# Amstrong number

num = int(input("enter the number"))
number = str(num)
amstrong = len(number)
sum_pow = sum(int(digit) ** amstrong for digit in number)
if num == sum_pow:
    print(f"{num} amstrong")
else:
    print(f"{num} not amstrong")