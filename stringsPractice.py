name = input("Enter your name: ")
salary = int(input("Enter your salary: "))
tax = salary * 0.16
pf = salary * 0.08
hra = salary * 0.04
total = salary + hra - tax - pf
print(f"\nsalary:\t{salary}\ntotal:\t{total}\ntax:\t{tax}\npf:\t{pf}\nhra:\t{hra}")
