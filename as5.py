num1 = int(input("Enter the number1..."))
num2 = int(input("Enter the number2..."))
operator = input("Choose operator (+,-,*,/)\t")
if operator == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation choose correct option")
