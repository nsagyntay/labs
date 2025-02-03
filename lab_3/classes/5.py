#Create a bank account class that has 
# attributes owner, balance and two 
# methods deposit and withdraw. 
#Withdrawals may not exceed the 
# available balance. Instantiate your 
# class, make several deposits and 
# withdrawals, and test to make sure
#  the account can't be overdrawn.
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")
owner = input("Enter account owner: ")
balance = float(input("Enter initial balance: "))
acc = Account(owner, balance)
deposit_amount = float(input("Enter deposit: "))
acc.deposit(deposit_amount)
withdraw_amount = float(input("enter withdraw: "))
acc.withdraw(withdraw_amount)




