def withdraw(balance,withdraw_amount):
    if withdraw_amount<balance:
        balance-=withdraw_amount
        print("with draw sucessful",balance)
    else:
        print("in sufficient funds")


def deposit(balance,deposit_amount):
    balance+=deposit_amount
    print("account balance",balance)
    print("Deposit sucessful")


account_holder_name=input("enter your name")
account_number=int(input("Enter account number"))
account_balance=float(input("Enter your balance"))
print("\tSWISS BANK")
print("******************")
print("Account holder name: ",account_holder_name)
print("Account number: ",account_number)
withdraw(account_balance,1234)

deposit(account_balance,7777)