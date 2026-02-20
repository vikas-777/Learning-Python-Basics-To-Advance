# String input: input()
# Type Casting: one data type into another data type
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print("sum of", num1, "and", num2, "is", total)
total *= 2
print("Multiplication operator: ", total)
total -= 2
print("Subtraction operator: ", total)
total += 2
print("Addition operator: ", total)
total /= 2
print("Divison operator: ", total)
total %= 2
print("remainder opeator: ", total)
x = int(input("Enter the 1st value: "))
y = int(input("Enter the 2nd value: "))
z = x == y
print(z)
p = int(input("Enter the 1st value: "))
q = int(input("Enter the 2nd value: "))
r = p == q
print(r)
print("And operation: ", z and r)
print("Or operation: ", z or r)
print("Not operation: ", not z)
