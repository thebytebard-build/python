import random
import sys
import abc
import datetime

class Utils:
    history=[]
    @staticmethod
    def gen_random():
        ano='' 
        for i in range(12):
            ano+=str(random.randint(1,9))
        return ano
    @classmethod
    def addentry(cls,msg):
        cls.history.append(msg)
    @staticmethod
    def createaccount(accounttype):
        if accounttype=='Savings':
            name=input('enter your name :')
        else:
            name=input('enter your Company name :')
        balance=eval(input('enter the balance :'))
        while balance<0:
            balance=eval(input('initial balance should not be negative please enter valid number:'))  
        if accounttype=='Savings':
            account=Savingaccount(name,balance)
        else:
            account=Currentaccount(name,balance)
        Utils.addentry('{} \n{} account has created with a/c no {}:'.format(datetime.datetime.now(),accounttype,account.ano))
        print('Congratulation your {} account has created with a/c no : {}'.format(accounttype,account.ano))
        return account
    
    @classmethod
    def detailedstatement(cls):
        print(cls.history[0])
        print('your {} last transaction are'.format(len(cls.history)-1))
        print('#'*50)
        no=1
        for transaction in cls.history[1:]:
            print('{}.  {}'.format(no,transaction))
            no+=1

    @classmethod
    def ministatement(cls):
        print(cls.history[0])
        if (len(cls.history)-1)<=5:
            print('your {} last transaction are'.format(len(cls.history)-1))
            print('#'*50)
            no=1
            for transaction in cls.history[1:]:
                print('{}.  {}'.format(no,transaction))
                no+=1 
        else:
            print('your last 5 transactions are')
            print('#'*50)
            no=1
            for transaction in cls.history[-5:]:
                print('{}.  {}'.format(no,transaction))
                no+=1



class Account(abc.ABC):
    BANKNAME='State Bank Of India'
    tlimit=0
    withdraw_amount=0
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
        self.ano=Utils.gen_random()
    
    def deposit(self):
        amount=eval(input('Enter amount to deposit :'))
        while amount<=0:
            amount=eval(input('Amount should be positive, please enter again :'))
        self.balance+=amount
        a.tlimit+=1
        if a.tlimit>5:
            self.balance-=10
        print('additional charge as number of transaction exceeds')
        Utils.addentry('{} Account credited(deposit) with accpunt : {}'.format(datetime.datetime.now(),amount))
        print('After deposit your account balance : {}'.format(self.balance))
    
    def withdraw(self):
        amount=eval(input('Enter amount to deposit :'))
        while amount<=0:
            amount=eval(input('Amount should be positive, please enter again :'))
        while amount%100!=0:
            amount=eval(input('Amount should be mutiple of 100, please enter again :'))
        if self.balance-amount>=self.min_balance:
            if Account.withdraw_amount+amount<=20000:
                self.balance-=amount
                Account.withdraw_amount+=amount
                a.tlimit+=1
                if a.tlimit>5:
                     self.balance-=10
                print('additional charge as number of transaction exceeds')
                Utils.addentry('{} Account debited(withdraw) with accpunt : {}'.format(datetime.datetime.now(),amount))
                print('After withdraw your account balance : {}'.format(self.balance))
            else:
                print('withdraw limit has exceedd')
        else:
            print('Sorry, insufficient fund')
        

       
            
class Savingaccount(Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,0) 
    def BalanceEnquiry(self):
        print('hey {} , Balance in your Saving accounts, ends with xxxxxxxxx{} is {}'.format(self.name,self.ano[9:],self.balance))
    def getAccountinfo(self):
        print('Your Savings Account Information')
        print('Account number :',self.ano)
        print('Customer name :',self.name)
        print('Current balance :',self.balance)
        print()
class Currentaccount(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,-1000)
    def BalanceEnquiry(self):
        print('hey {} , Balance in your Current accounts, ends with xxxxxxxxx{} is {}'.format(self.name,self.ano[9:],self.balance))
    def getAccountinfo(self):
        print('Your Current Account Information')
        print('Account number :',self.ano)
        print('Customer name :',self.name)
        print('Current balance :',self.balance)
        print()

print('Welcome to',Account.BANKNAME)
print('Do you want to open Current account or Saving account')
print('s-for saving acoount and c-for current account')
option=input('enter your choice : ').lower()
count=1
while option not in ['s','c']:
    if count>=3:
        print('max numbers of attempts have reached')
        sys.exit()
    option=input('please select valid option [s/c] : ').lower()
    count+=1

if option=='s':
    a=Utils.createaccount('Savings')
else:
    a=Utils.createaccount('Current')


for x in Utils.history:
            print(x)

tlimit=0
while True:
    print('b-Balance enquiry\nd-Deposit\nw-Withdraw\nms-Mini statement\nds-detailed statement\ng-Get account information\ne-Exit')
    option=input('enter your choice : ').lower()
    count=1 
    while option not in ['b','d','w','ms','ds','g','e']:
        if count>=3:
            print('max numbers of attempts have reached')
            sys.exit()
        option=input('Invalid option, Enter correct option [b|d|w|ms|ds|g|e] : ').lower()
        count+=1
    if option=='b':
        a.BalanceEnquiry()
    elif option=='g':
        a.getAccountinfo()
    elif option=='d':
        a.deposit()
    elif option=='w':
        a.withdraw()
    elif option=='ds':
        Utils.detailedstatement()
    elif option=='ms':
        Utils.ministatement()
    else:
        print('Thanks for using state bank of india application')
        sys.exit()
    print()
        

