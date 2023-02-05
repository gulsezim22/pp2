class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f'Account owner:{self.owner}\nAccount balance: ${self.balance}'
    def deposit(self,depreplenish):
        self.balance += depreplenish
        print("Accepted")
    def withdraw(self,wdeliminate):
        if self.balance >= wdeliminate:
            self.balance -= wdeliminate
            print("Eliminated")
        else:
            print("Unavailable!")
account1 = BankAccount("Gulsezim",500)
print(account1)