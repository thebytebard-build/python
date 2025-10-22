#little project from lecture of oops
import sys

class Movie:
    '''this is movie class . you have to pass movie title hero herione name at the time of making object and you can get information through info function'''
    def __init__(self,title,hero,herione):
        self.title=title
        self.hero=hero
        self.herione=herione

    def info(self):
        print('title of the move :',self.title)
        print('hero of the move :',self.hero)
        print('herione of the move :',self.herione)

def numbermovie(n):
    list_of_movie=[]

    while True:
        title=input('enter movie title : ')
        hero=input('enter movie hero : ')
        herione=input('enter movie herione : ')
        m=Movie(title,hero,herione)
        list_of_movie.append(m)
        print('movie added successfully....')
        option=input('do you want to add new movie enter [yes/no] : ')
        if option.lower()=='no':
            break

    print('all movies information.....')
    print('#'*40)
    for movies in list_of_movie:
        movies.info()
        print()



class Customer:
    '''customer describe to use bank operation. you have to pass name and balance but balance is not compulsory at the time of object creation and you have wo facility deposit and withdraw'''
    bankname='durgasoft'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deopsit(self,amt):
        '''you have to pass amount then it will add and print new amt'''
        self.balance+=amt
        print('balance after deposit :',self.balance)
    def withdraw(self,amt):
        '''here you have to pass amt but amt should be bigger than current amt '''
        if amt>self.balance:
            print('insufficient fund ')
            sys.exit()
        self.balance-=amt
        print('balance after withdraw :',self.balance)


#inner class
class Human:
    def __init__(self,name):
        print('human creation')
        self.name=name
        self.head=self.Head()
    def info(self):
        print('hello myself',self.name)
        print('im fully busy with')
        self.head.talk()
        self.head.Brain.think()
    class Head:
        def __init__(self):
            print('head creation')
            self.Brain=self.Brain()
        def talk(self):
            print('thinking')
        class Brain:
            def __init__(self):
                print('brain creation')
            def think(self):
                print('thinking')

# inheritance
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatdrink(self):
        print('eat biryani and drink coke')

class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    @staticmethod
    def work():
        print('coding python...')
    def einfo(self):
        print(self.name,self.age,self.eno,self.esal)
        
#hybrid inheritance to find mro
class A:
    pass 
class B:
    pass  
class C:
    pass   
class X(A,B):
    pass   
class Y(B,C):
    pass   
class P(X,Y,C):
    pass 

#print(P.mro())


