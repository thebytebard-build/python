# functions part 1

#take two args and return sum
def sum(a,b):
    return a+b

#area of circle
def area_circle(r):
    return 3.14*r**2

#average of three number
def average(a,b,c):
    return sum(a,b,c)/3

#compound interest
def compound(p,r,t):
    return (p*(1+r/100)**t)-p

#volume of cuboid
def v_cuboid(a,b,c):
    return a*b*c

#check if number is 7
def check_seven(a):
    return True if a==7 else False

#find greater among three number
def find_g(a,b,c):
    return max(a,b,c)

#check whther a number is prime or not
def find_p(n):
    for x in range(2,n):
        if n%x==0:
            return False
    return True

#check if year is leap year
def check_leap(y):
    if y%100==0 and y%400==0:
        return True
    if y%100!=0 and y%4==0:
        return True
    return False

#factorial of a number
def factorial(n):
    m=1
    for x in range(1,n+1):
        m*=x
    return m

#printfirst natural odd number
def odd(n):
    for x in range(1,n+1,2):
        print(x)
        
#first n prime number
def first_p(n):
    p=2
    count=0
    while True:
     for x in range(2,p):
        if p%x==0:
            break
     else:
         print(p)
         count+=1
     if count==n:
        break
     p+=1
    
#prime number between two values
def between_p(s,e):
    for n in range(s+1,e):
     for x in range(2,n):
        if n%x==0:
            break
     else:
         if n!=1:
          print(n)
    
#first n fibonacci series
def fibonacci(n):
    aft=1
    prev=0
    for x in range(n):
        print(prev)
        prev,aft=aft,prev+aft
        
#print all factors of given numbers
def factor(n):
    if n==0:
        print(0)
        return
    for x in range(1,n+1):
        if n%x==0:
            print(x)

factor(69)