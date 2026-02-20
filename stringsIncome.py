name = input("Enter your name : ")
salary = int(input("Enter your salary : "))
tax = salary * 0.12
pf = salary * 0.06
hra = salary * 0.04
total = salary + hra - tax - pf
print(
    f"name\tsalary\ttax\thra\ttotal\n***************************************\n{name}\t{salary}\t{tax}\t{pf}\t{hra}\t{total}")
