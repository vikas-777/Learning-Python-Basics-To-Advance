def square(num):
    return num ** 2


def cube(num):
    return num ** 3

print("Available options")
print("------------------")
print("1.square")
print("2.cube")
print("3.exit")
op = input("Enter the choice")
number = int(input("Enter the number"))
square_num = square(number)
qube_num = cube(number)
if op == "1":
    print(f"square of {number} = {square_num}")
elif op == "2":
    print(f"cube of {number} = {qube_num}")
else:
    print("Exiting....")