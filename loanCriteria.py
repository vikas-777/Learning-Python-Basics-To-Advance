def loan_eligibility(name,age,amount):
    if age >=21 and amount>=25000:
        print(f"{name} you are eligible")
    else:
        print(f"{name} you are not eligible")
    return name,age,amount


name = input("Enter your name: ")
age = int(input("Enter your age: "))
amount = int(input("Enter the amount: "))


# loan_eligibility(name,age,amount)
loan_eligible = loan_eligibility(name,age,amount)
print(f"By using return statement {loan_eligible}")