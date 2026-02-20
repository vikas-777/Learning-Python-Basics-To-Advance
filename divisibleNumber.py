x = int(input("Enter the number...."))
if x % 5 == 0 and x % 10 == 0:
    print(f"{x} Divisible by both 5 and 15")
elif x % 5 == 0:
    print(f"{x} Is divisible by 5 but not 15")
else:
    print(f"{x} Not divisible by any of the one number")
