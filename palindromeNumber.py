num = int(input("Enter the number: "))
og_num = num
rev_num = 0
for i in str(num):
    rev_num = rev_num * 10 + num % 10
    num = num // 10
if og_num == rev_num:
    print(f"{og_num} is palindrome")
else:
    print(f"{og_num} not a palindrome")



