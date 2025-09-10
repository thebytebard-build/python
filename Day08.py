#forloopS

#1 print till n
n=int(input("enter a number : "))
for i in range(1,n+1):
    print(i)
       

#2 print from n to 1
n=int(input("enter a number : "))
for i in range(n,0,-1):
    print(i)

#3print from start to end
start=int(input("enter a number : "))
end=int(input("enter a number : "))
for i in range(start+1,end+1):
    print(i)
    

#sum of 1 to 10    
sum=0
for i in range(1,10+1):
    sum=sum+i
print("sum is",sum)


#print product of 1 to 10
multiply=1
for i in range(1,10+1):
    multiply=multiply*i
print("multiply is",multiply)


#check from 1 to 100 how many numbers are divisible by 7
for i in range (1,100+1):
    if i%7==0:
        print(i)
    

#check from 1 to 200 how many numbers are divisible by 7 and 6
for i in range(1,200+1) :
    if i%7==0 and i%6==0:
        print(i)
    


#sum of 20 to 50 that are divisible by 4
sum=0
for i in range(20,50+1):
    if i%4==0:
        print(i)
        sum+=i
print("sum of numbers: ",sum)

#print the table of n
n=eval(input('enter a number for a table : '))
for i in range(1,10+1):
    print(n,'*',i,'=',n*i)

    
#print the factorial of n
n=eval(input('enter a number for a factorial : '))
f=1
for i in range(1,n+1):
    f*=i
print("factorial : ",f)

#take two input x and y if x<y then print x to y and vice versa also
x=eval(input('enter a number :'))
y=eval(input('enter a number :'))
if x<y:
    for i in range(x,y+1):
        print(i)
elif y<x:
    for i in range(y,x+1):
        print(i)
else:
    print("both are same")

#loop part 2

#print each charcter of string with its unicode value
s=input("enter a string : ")
for x in s:
    print(x,'=',ord(x))

#print only vowels present in the string
s=input("enter a string : ")
for x in s:
    if x in 'aeiouAEIOU':
        print(x)

# count the spaces
s=input("enter a string : ")
i=0
for x in s:
    if x==' ':
        i+=1
print(i)
#s.count(' ')

#print all unique digit of n
n=int(input("enter the number : "))
i=0
d=str(n)
s=' '
for x in d:
    if s==' ' or x not in s:
        s=s+d[i]
        print(x,end=',')
    i+=1

# count the digits in the number
n=int(input("enter the name : "))
i=0
for x in range(len(str(n))):
   if n!=0:
      i+=1
      n//=10
print(i)

#first m multiple of n
m=int(input("enter the number :"))
n=int(input('enter the number :'))
for x in range(m):
    print((x+1)*n)

#first m multiple of n in reverse order
n=int(input('enter the number :'))
for x in range(10,0,-1):
    print(x*n)

    
# user choice table
n=int(input('enter the number :'))
for x in range(10):
    print(n,'*',x+1,'=',(x+1)*n)


#first n even numbers
n=int(input("enter the number : "))
for x in range(2,2*10+1,2):
    print(x)

#first n odd numbers
n=int(input("enter the number : "))
for x in range(1,2*10,2):
    print(x)

#first n square
n=int(input("enter the number : "))
for x in range(n):
    print((x+1)**2)


#first n cube
n=int(input("enter the number : "))
for x in range(n):
    print((x+1)**3)

# print prime numbers within range of start and end
start=int(input("enter the number : "))
end=int(input("enter the number : "))
for x in range(max(2,start+1),end):
    for d in range(2,x):
        if x%d==0:
            break
    else:
        print(x)

# sum of first n natural number
n=int(input("enter the number : "))
sum=0
for x in range(n):
    sum+=x+1
print(sum)

# sum of first square of n natural number
n=int(input("enter the number : "))
sum=0
for x in range(n):
    sum+=(x+1)**2
print(sum)


# sum of first cube of n natural number
n=int(input("enter the number : "))
sum=0
for x in range(n):
    sum+=(x+1)**3
print(sum)

        
# sum of first n odd number
n=int(input("enter the number : "))
sum=0
for x in range(1,2*n,2):
    sum+=x
print(sum)

# sum of first n even number
n=int(input("enter the number : "))
sum=0
for x in range(2,2*n+1,2):
    sum+=x
print(sum)

# factorial of n
n=int(input("enter the number : "))
f=1
for x in range(n):
    f=f*(x+1)
print(f)

# summ of digits of n 
n=int(input("enter the number : "))
sum=0
for x in range(len(str(n))):
    if n!=0:
       sum+=n%10
       n//=10
print(sum)

# convert decimal to binary
n=int(input("enter the number : "))
s=""
for _ in range(n):
    if n==0:
        break
    s=s+str(n%2)
    n=n//2
print(s[::-1])

# convert decimal to octal
n=int(input("enter the number : "))
s=""
for _ in range(n):
    if n==0:
        break
    s=s+str(n%8)
    n=n//8
print(s[::-1])