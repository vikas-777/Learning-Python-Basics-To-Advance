# n = int(input("Enter the no.."))
# a, b = 0, 1
# i = 0
# if n<=0:
#     print("Please enter positive number")
# elif n==1:
#     print(a)
# else:
#     while i < n:
#         print(a,end=" ")
#         a, b = b, a + b
#         i += 1

################################################
num = int(input("Enter number "))
num1 = 1
num2 = 2
i = 0
for i in  range(num):
    num = num1 + num2
    num1 = num2
    num2 = num
    print(num)