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

#lcm of two number
def lcm(a,b):
    l=[]
    i=2
    while a!=1 or b!=1:
        while i<=max(a,b):
            if (a!=1 and a%i==0) or (b!=1 and b%i==0):
                if (a!=1 and a%i==0):
                    a=a//i
                if (b!=1 and b%i==0):
                    b=b//i
                l.append(i)     
            else:
                i+=1    
    m=1
    for x in l:
        m*=x
    return m
            
#count words of string
def word_string(s):
    s1=s.rstrip()
    s2=s1.lstrip()
    return s2.count(' ')+1

#create list of between two prime number
def between_p(s,e):
    l=[]
    for n in range(s+1,e):
     for x in range(2,n):
        if n%x==0:
            break
     else:
         if n!=1:
          l.append(n)
    return l

#from a string create a list then make dictionary the first letter of word would be the key and all word starting from same letter would be the values
def dict_from_list(s):
    l=s.split()
    l2=[]
    d={}
    for x in l:
        if x[0] not in d:
            d[x[0]]=[x]
        else:
            d[x[0]].append(x)
    print(d)

#find common factor of two given number
def common_factore(a,b):
    t=[]
    for x in range(2,min(a,b)+1):
        if a%x ==0 and b%x==0:
            t.append(x)
    tt=tuple(t)
    print(tt)

#remove duplicate from list
def remove_d(l):
    s=set(l)
    l=list(s)
    return l

# count frequency of each element in list and store their element as key and frequency as value in dict
def fre(l):
    s=set(l)
    d={}
    for x in s:
        d[x]=l.count(x)
    return d

#find number in a given text then store in list and return list
def find_n(s):
    l=[]
    for x in s:
        if x.isdigit():
            l.append(x)
    return l

# find largest sorted  subsequence
def find_largest(l):
    l1=[]
    l2=[]
    i=0
    while i<len(l)-1:
        if l[i]<=l[i+1]:
            if not l1:
              l1.append(l[i])
            l1.append(l[i+1])
        else:
            if l1:
             l2.append(l1.copy())
             l1.clear()
        i+=1
    if l1:
        l2.append(l1)
    i=0
    ll=[]
    for x in l2:
        if i<len(x):
            i=len(x)
            ll=x.copy()
    print(ll)
        

# find if two list have same element in any order
def find_same(l1,l2):
    for x in l1:
        if x not in l2:
            return False
    return True



dict_from_list("radha rani badi pyari badi syani")