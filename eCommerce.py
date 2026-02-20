inventory = {"apple": 200, "ball": 300, "cat": 500, "dog": 1000}
stock = {"apple": 100, "ball": 100, "cat": 100, "dog": 100}
users = {"user": "user123", "admin": "admin123"}
cart = {}


def login():
    print("login")
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("login successful! \n")
        return True
    else:
        print("invalid user name or password \n")
        return False


def check_stock(item, quantity):
    return stock.get(item, 0) >= quantity


def add_to_cart(item, quantity):
    if item in inventory:
        if check_stock(item, quantity):
            cart[item] = cart.get(item, 0) + quantity
            stock[item] -= quantity
            print(f"added{quantity} {item} (s) to cart\n")
        else:
            print(f"{stock[item]} {item} left in cart\n")
    else:
        print("item not fount\n")

def remove_from_cart(item):
    if item in cart:
        stock[item] += cart[item]
        del cart[item]
        print(f"{item} removed from cart")
    else:
        print("Item not in cart\n")


def calculate_bill():
    total = 0
    for item, quantity in cart.items():
        total += inventory[item] * quantity
    if total >= 2000:
        discount = total * 0.20
        total -= discount
    return total


def print_invoice():
    print("\n\tInvoice")
    print("----------------------------")
    for item, quantity in cart.items():
        price = inventory[item]
        print(f"{item.title()} x {qty} = {price * qty} INR")
    print("----------------------------")
    print("Total Payable:", calculate_bill(), "INR")
    print("----------------------------\n")


if login():
    while True:
        print("1. Add to Cart")
        print("2. Remove from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ").lower()
            qty = int(input("Enter quantity: "))
            add_to_cart(item, qty)

        elif choice == '2':
            item = input("Enter item to remove: ").lower()
            remove_from_cart(item)

        elif choice == '3':
            print("\nYour Cart:", cart, "\n")

        elif choice == '4':
            print_invoice()
            break

        elif choice == '5':
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice!\n")
