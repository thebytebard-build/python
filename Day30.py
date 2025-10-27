from abc import ABC,abstractmethod

class Account(ABC):
    def __init__(self,name,balance,min_bal):
        self.name=name
        self.balance=balance
        self.min_bal=min_bal
    def __averageBalance__(self):
        pass
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_bal:
            self.balance-=amount
            self.__averageBalance__()
        else:
            print('insufficient fund')
    @abstractmethod
    def accountinfo(self):
        pass

class Savingaccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,0)
    def __str__(self):
        return "it is {} saving account with balance {} and minmum balance {}".format(self.name,self.balance,self.min_bal)
    def accountinfo(self):
        print("it is {} saving account with balance {} and minmum balance {}".format(self.name,self.balance,self.min_bal))
    
class Currentaccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,-1000)
    def __str__(self):
        return "it is {} current account with balance {} and minimum balance {}".format(self.name,self.balance,self.min_bal)
    def accountinfo(self):
        print("it is {} current account with balance {} and minimum balance {}".format(self.name,self.balance,self.min_bal))

s=Savingaccount('roshani',50000)
print(s)
s.deposit(5300)
s.accountinfo()
s.withdraw(10000000)