class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def Diposit(self,amount):
        self.balance +=amount
        print(f'Hello {self.owner} new balance in account is {self.balance}')
    def Withdraw(self,amount):
        if(amount > self.balance):
            print(f'Hey {self.owner} insufficent balance please enter a amount less then {self.balance-500}')
        else : 
            self.balance -= amount
            print(f'Hello {self.owner} new balance in account is {self.balance}')
    
    def CheckBalance(self):
        print(self.balance)

SBI = BankAccount("Jayesh",10000000)
SBI.CheckBalance()
SBI.Withdraw(2000)
SBI.Diposit(500000)