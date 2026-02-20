def loan_eligibility(name, age, amount):
    if age >= 21 and amount >= 25000:
        print(f"{name} you are eligible ")
    else:
        print(f"{name} you are not eligible ")
    return name, age, amount


def intrest(amount, rate, time):
    return amount * (rate * 0.01) * time


def total_payable(intrest, amount):
    return intrest + amount


name = input("Enter your name: ")
age = int(input("Enter your age: "))
amount = int(input("Enter the amount: "))
rate = int(input("Enter the rate of intrest"))
time = int(input("Enter the number of years"))

si = intrest(amount, rate, time)
total = total_payable(si, amount)
print(f"Intrest {si}")
print(f"Total payable {total}")
