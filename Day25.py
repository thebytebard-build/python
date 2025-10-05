#leccture random module program 

from random import *

#generate n six digit otp
def otp(n):
    for x in range(n):
        print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')




#generate six digit number alphabetdigitalphabetdigitalphabetdigit like T5G8D6
def digit(n):
    digit='123456789'
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(n):
        print(choice(digit),choice(alphabet),choice(digit),choice(alphabet),choice(digit),choice(alphabet),sep='')




#generate fake employee data and take how many fake emplyee data 
def employee_data(number):

    alphabet='abcdefghijklmnopqrstuvwxyz'
    digit='0123456789'
    city=['hyderabad','pune','delhi','bengalore','chennai','mumbai']
    d=['senior software enginner','software enginner','team lead','project lead','project manager']

    #fake name
    def fake_n():
        name=choice(alphabet).upper()
        n=randint(2,9)
        for i in range(n):
            name+=choice(alphabet)
        return name
    
    #fake employee number
    def fake_num():
        number="e-"
        for i in range(4):
            number+=choice(digit)
        return number
    
    #fake employee salary
    def fake_s():
        return uniform(10000,50000)
    #fake city name
    def fake_c():
        return choice(city)
    
    #fake mobile number
    def fake_m():
        m=choice('6789')
        for i in range(9):
            m+=choice(digit)
        return m

    #fake designation
    def fake_d():
        return choice(d)

    #fake employee data
    def data():
        print('Employee name :',fake_n())
        print('Employee number :',fake_num())
        print('Employee salary : {:.2f}'.format(fake_s()))
        print("Employee city :",fake_c())
        print('Employee mobile :',fake_m())
        print('Employee designation :',fake_d())

    for i in range(number):
        data()
        print()

employee_data(2)