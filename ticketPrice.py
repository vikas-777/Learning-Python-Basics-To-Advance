user = (input("Hey user enter your name..."))
age = int(input("Enter your age..."))
if age <= 12:
    print(f"Dear {user}the ticket price is 20 Rupees")
elif age <= 60:
    print(f"Dear {user} the ticket price is 40 Rupees")
else:
    print(f"Dear {user} the ticket price is 30 Rupees")
