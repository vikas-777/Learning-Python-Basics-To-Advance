def bill(Quantity):
    price = 100
    total = price * Quantity
    if total >= 1000:
        discount = total * 0.10
        return total - discount
    else:
        return total


Quantity = int(input("Enter quantity: "))
payable = bill(Quantity)
print(f"\t Invoice")
print(f"--------------")
print(f"Qunatity ------ Total\n\t{Quantity}\t------ \t{payable}")
