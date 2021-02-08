class bankAccount():
    def set_details(self,name=0,balance=0):
        self.name = name
        self.balance = balance
    def display(self):
        print(f'The name is {self.name}')
        print(f'The balance is {self.balance}')
    def withdraw(self,amount):
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
        
b1 = bankAccount()
b2 = bankAccount()

b1.set_details('Mike',30)
b1.display()
b1.withdraw(10)
print(f'The balance after withdrawal is {b1.balance}')
b1.deposit(100)
print(f'The balance after deposit is {b1.balance}')

b2.set_details()
b2.display()
b2.withdraw(10)
print(f'The balance after withdrawal is {b2.balance}')
b2.deposit(100)
print(f'The balance after deposit is {b2.balance}')