# function part 3 (100 question )

# this file has three section 1) Basic  2) Intermediate  3)Advanced

# 1) Basic 1 to 25 question

# print hello world
def p_hw():
    print('Hello, World!')

#take name and print greeting
def greet(s):
    print("! Hope you’re having a great day!")

#a functio that return square of number
#with lambda function
sq=lambda n:n*n

#add two numbers
add=lambda x,y:x+y

#maximum of two number
maxm=lambda x,y: x if x>y else y

#length of string
def count(s):    
    return sum(1 for _ in s)

#check if even or odd
cOddEven=lambda n:'even' if n%2==0 else 'odd'

#factorial of number
def factoial(n):
    from functools import reduce
    return 0 if n==0 else reduce(lambda x,y:x*y,range(1,n+1))

#return cube of a number
cube =lambda n:n**3

#are of circle
area_c=lambda r:3.14*r**2

#calculate simple interest
si=lambda p,r,t: (p*r*t)/100

#check if number is prime
def check_p(n):
    for x in range(2,n):
        if n%x:
            return False
    return True

#count vowels
def count_v(s):
    return sum( 1 for x in s if x.lower() in 'aeiou' )

#convert celcius into fahrenhite
c_f=lambda c: (9/5*c)+32

#convert fahrenhite into celcius
f_c=lambda f:5*9(f-32)

#reverse a string


# 2) Intermediate 26 to 60 questions

#check if number is perfect square
def check_square(n):
    l=[]
    if n==0:
        return
    else:
     for x in range(2,n+1):
        while n%x==0:
            l.append(x)
            n=n//x
        if n==1:
            break
     for x in range(0,len(l),2):
        if l.count(l[x])%2!=0:
            return False
     return True

#calculate power of number
def cal_power(n,p):
    return n**p

#print first n fibonacci number
def fibonacci(n):
    aft=1
    prev=0
    for i in range(n):
        print(prev)
        prev,aft=aft,aft+prev

#print nth fibonacci number
def nth_fibonacci(n):
    aft=1
    prev=0
    for i in range(n-1):
        prev,aft=aft,aft+prev
    print(prev)   

#check if string contain only alphabet 
#without inbuilt function
def onlyAlpha(s):
    digit="123456789"
    for x in s:
        if x in digit:
            return False
    return True
#with inbuilt function
def only_alpha(s):
    return s.isalpha()

#check if two string are anagram
def anagram(s1,s2):
    if s1!=s2 and len(s1)==len(s2):
        for x in s1:
            if x in s2:
               pass
            else:
                return False
        return True
    return False

#remove all spaces from string and return string
def remove_space(s):
    return s.replace(' ','')

#return absolute value
#with inbuilt funciton
def absolute(n):
    return abs(n)
#without inbuilt function
def abolutee(n):
    return n if n>=0 else n-n*2

#return ascii value of character
def ascii(ch):
    return ord(ch)

#calculate compound interest
def compound(p, r, t):
    return p*(1+r/100)**t- p

#check if number is armstrong
def check_armstrong(n):
    n1=n
    l=[]
    sum=0
    i=0
    while n1!=0:
        l.append(n1%10)
        n1=n1//10
        i+=1
    for x in l:
        sum+=x**i
    if sum==n:
        return True
    return False
#shorter with chatgpt help
def armstrong(n):
    l=[int(x) for x in str(n)]
    return sum(x**len(l) for x in l)==n
    
#check if number is perfect
def checkperfect(n):
    l=[]
    for x in range(1,n):
        if n%x==0:
            l.append(x)
    return n==sum(l)

#multiplication table
def table(n):
    for x in range(1,11):
        print(n,'*',x,'=',n*x)

#find gcd of two number
def gcd(n1,n2):
    m=1
    for x in range(2,min(n1,n2)+1):
        while n1%x==0 and n2%x==0:
            n1=n1//x
            n2=n2//x
            m*=x
    return m       

#find lcm of two number
def lcm(a,b):
    m=1
    for x in range(2,max(a,b)+1):
        while (a!=1 and a%x==0) or (b!=1 and b%x==0):
            if a!=1 and a%x==0:
                a=a//x
            if b!=1 and b%x==0:
                b=b//x
            m*=x
    return m
            
#flatten a list
def flatten(l):
    l2=[]
    for x in l:
        if type(x)==int:
            l2.append(x)
        else:
          for i in x:
            l2.append(i)
    return l2

#merge two sorted list
def merge_sorted(l1,l2):
    l3=[*sorted(l1),*sorted(l2)]
    return l3

#remove duplicate from list
def remove_dup(l):
    s=set(l)
    l=list(s)
    return l

#write a function to retuen frequencey of each character 
def fre(s):
    d={}
    for x in s:
        d[x]=d.get(x,0)+1
    return d

#find second largest element of list
def second_lar(l):
    l.sort()
    return l[-2]

#find common element of two list
def common(l1,l2):
    l3=[]
    for x in l1:
        if x in l2:
            l3.append(x)
    return l3

#write function that sort a list wiithut sort
def sort_list(l):
    l2=[]
    while l:
        l2.append(min(l))
        l.remove(min(l))
    l[:]=l2 
    return l

#take list and posiitons and rotate a list by k position
def rotate(l1,k):
    k=k%len(l1)
    l2=[]
    i=len(l1)-k
    while i<len(l1):
        l2.append(l1[i])
        l1.remove(l1[i])
    for x in l1:
        l2.append(x)
    return l2

#intersection of two sets
def inter(s1,s2):
    s3=set()
    for x in s1:
        if x in s2:
            s3.add(x)
    return s3

#union of two set(s1,s2)
def union(s1,s2):
    s3=set(s1)
    s3.update(s2)
    return s3

#return list of prime number in a given range
def pr(start,end):
    l=[]
    for x in range(start+1,end+1):
        for i in range(2,x):
            if x%i==0:
                break
        else:
            l.append(x)
    return l

#for ncr and npr quesstion we need a function of factorial
def fact(n):
    m=1
    for x in range(1,n+1):
        m*=x
    return m

#calculate combination(ncr)
def ncr(n,r):
    return fact(n)//(fact(r)*fact(n-r))

#calculate permutation(npr)
def npr(n,r):
    return fact(n)//fact(n-r)

#count uppercase and lowercase letter
def count_UandL(s):
    count_u=0
    count_l=0
    for x in s:
        if x.islower():
            count_l+=1
        if x.isupper():
            count_u+=1
    return count_u,count_l

#capitalize the first letter of each word
def capitalize(s):
    i=0
    result=''
    while i<len(s):
        if s[0].isalpha() and i==0:
            result+=s[i].upper()
        elif s[i].isalpha() and s[i-1]==' ':
            result+=s[i].upper()
        else:
            result+=s[i]
        i+=1
    return result
        
#remove punctuation from string
def remove_p(s):
    for x in s:
        if x.isalnum() or x.isspace():
            pass
        else:
            s=s.replace(x,'')
    return s

#longest word in string
def l_w(s):
    l=s.split()
    w=""
    for x in l:
        if len(x)>len(w):
            w=x
    return w

#smallest word odf string
def s_w(s):
    l=s.split()
    w=l[0]
    for x in l:
        if len(x)<len(w):
            w=x
    return w

#frequency of each word in string
def freq(s):
    l=s.split()
    d={}
    for x in l:
        d[x]=d.get(x,0)+1
    return d

#check if year is leap year or not
def leap(n):
    if n%100==0 and n%400==0:
        return True
    elif n%100!=0 and n%4==0:
        return True
    return False


############
# 3) Advanced
############

#make star pyramid
def star_pyramid(n):
    for x in range(n):
        for i in range(n-x):
            print(' ',end='')
        for j in range(x+1):
            print('* ',end='')
        print()

#make diamond pattern
def diamond(n):
    for x in range(n):
        for i in range(n-x):
            print(' ',end='')
        for j in range(x+1):
            print('* ',end='')
        print()
    n=n-1
    for x in range(n):
        for j in range(x+1):
            print(' ',end='')
        for i in range(n-x):
            print(' *',end='')
        print()

#decimal into binary
def binary(n):
    s=''
    if n==0:
        print('0')
    else:
     while n!=0:
        s+=str(n%2)
        n=n//2
     print(s[::-1])

#decimal to octal
def octal(n):
    s=''
    if n==0:
        print('0')
    else:
     while n!=0:
        s+=str(n%8)
        n=n//8
     print(s[::-1])

#decimal to hexadecimal
def hexadecimal(n):
    s=''
    if n==0:
        print('0')
    else:
     while n!=0:
        if n%16>=10:
          s+=chr(65+((n%16)%10))
        else:
          s+=str(n%16)
        n=n//16
     print(s[::-1])

#binary to decimal
def b_to_d(n):
    n=int(n)
    sum=0
    p=0
    while n!=0:
        sum+=n%10*2**p
        n=n//10
        p+=1
    print(sum)

#int to roman number
#mycode
def roman():
    s=''
    i={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC',100:'C',200:'CC',300:'CCC',
       400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM',1000:'M'}
    n=int(input('enter a number : '))
    ns=str(n)
    it=1
    number=0
    new=''
    for x in ns:
        new=ns[it::]
        number=int(x)*10**len(new)
        s+=i[number]
        it+=1
    print(s)
#chatgpt code 
def roman():
    i = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }
    n = int(input("Enter a number: "))
    s = ""
    for k in sorted(i.keys(), reverse=True):
        while n >= k:
            s += i[k]
            n -= k
    print(s)


#roman number to int
def r_int():
    d = {
    "I": 1,"V": 5, "X": 10,"L":50,"C": 100,"D": 500,"M": 1000
    }
    ns=input('enter roman number : ').upper()
    sum=0
    prev=ns[0]
    for x in ns:
        if d[prev]>=d[x]:
            sum+=d[x]
            prev=x
        else:
            sum+=(d[x]-d[prev]*2)
            prev=x
    print(sum)

#check if string is panagram
def panagram(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    for x in alpha:
        if x not in s.lower():
            print("no, it is not panagram")
            break
    else:
        print("yes it is panagram")

#generate pascal's triangle
#for this question i need to solve ncr which means combination so im using function that i have already made in intermediate section that is ncr
def pascal(r):
    for x in range(r):
        for j in range(r-x):
            print('',end=' ')
        for i in range(x+1):
            print(ncr(x,i),end=' ')
        print()


#sum of square of first n natural numbers
def ss(n):
    sum=0
    for x in range(1,n+1):
        sum+=x**2
    print(sum)

#sum of cube of first n natural numbers
def ss(n):
    sum=0
    for x in range(1,n+1):
        sum+=x**3
    print(sum)

#digital root of n
def dr(n):
    while n>=10:
        sum=0
        while n>0:
            sum+=n%10
            n=n//10
        n=sum
    print(sum)
#chatgpt
def dr(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    print(n)

#return all factors of number
def factor(n):
    l=[]
    for x in range(1,n+1):
        if n%x==0:
            l.append(x)
    return l

print(factor(45))

#print all subset of list 
#i made with help of chatgpt2
def generate_subsets(lst):
    subsets = [[]]  # Start with empty subset

    for elem in lst:
        # Create new subsets by adding the current element to existing subsets
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [elem])
        subsets += new_subsets  # Add new subsets to the list

    return subsets
