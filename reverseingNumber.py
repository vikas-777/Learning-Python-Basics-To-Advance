number = int(input("Enter the number: "))
temporary_variable = number
reverse  = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number//10
print(f"Reverse of {temporary_variable} = {reverse}")

#using for loop

n = int(input("Enter the number: "))
act_num = 0
for i in str (n):
    remainder1 = n%10
    act_num = act_num*10+remainder1
    n = n//10
print(act_num)

num = input("Enter number")

name =int(str(num)[::-1])

print(type(name))
print(name)