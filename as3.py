x = int(input("Enter the number..."))
if x % 3 == 0:
   print(f"{x} The number is divisible by 3")
elif x%5==0:
    print(f"{x} The number is divisible by 5")
elif x%3==0 and x%5==0:
    print(f"{x} The number is divisible by both 3 and 5")
else:
    print(f"{x} The number is not divisible by both 3 and 5")