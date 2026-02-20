number = int(input("Enter the number: "))
temporary_variable = number
reverse  = 0
while number > 0:
    remainder = number % 10
    reverse = reverse * 10 + remainder
    number = number//10
print(f"Reverse of {temporary_variable} = {reverse}")
