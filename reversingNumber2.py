number = int(input("Enter the number..."))
my_var = number
rev_num = 0
for i in range(number):
    remainder = number % 10
    rev_num = rev_num * 10 + remainder
    number = number // 10
    if i > number:
        break
print(f"Reversed number of {my_var} = {rev_num}")


