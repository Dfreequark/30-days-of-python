'''
Implement a class called BankAccount with attributes account number, account holder name, and balance. 
Include methods to deposit and withdraw money from the account.
'''

class BankAccount():
    def __init__(self, ac_no, name, balance):
        self.ac_no = ac_no
        self.name= name.upper()
        self.balance= balance
    def ac_details(self):
        return {"Account Number :": self.ac_no, " Name: ": self.name, " Balance: ": self.balance}
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
account= BankAccount(ac_no=1234, name="alice", balance=1000)

print(account.ac_details())

account.deposit(10000)
print(account.ac_details())

account.withdraw(2000)
print(account.ac_details())
