#if else part 2

# Compare two numbers and print the greatest
a=eval(input("enter a number :"))
b=eval(input("enter a number :"))
if a>b:
    print("Greatest number",a)
elif b>a:
    print("Greatest number",b)
else:
    print("both are same",a)

# Compare two strings in dictionary order
a=input("enter a string :")
b=input("enter a string :")
if a<b:
    print("In dictionary order",a,b)
else:
    print("In dictionary order",b,a)

# Check if a number is three-digit
n=eval(input("enter a number :"))
if n/100>=0:
    print("it is a three digir number")
else:
    print("it is a three digir number") 

# Find nature of roots for quadratic equation
print("ax**2 + bx + c this is the equation now eneter a,b,c values ")
a=eval(input("enter a number :"))
b=eval(input("enter a number :"))
c=eval(input("enter a number :"))
d=b**2-4*a*c
if d>0:
    print("Two real & distinct roots")
elif d<0:
    print("Imaginary (complex) roots")
else:
    print("Two real & equal roots (also called repeated or coincident roots)")

# Check leap year
y=int(input("enter the year"))
if y%4==0 and y%100!=0 :
    print("it is leap year")
elif y%400==0 and y%100==0:
    print("it is leap year")
else:
    print("it is not leap year") 

# Find greatest among three numbers
a=eval(input("enter a number :"))
b=eval(input("enter a number :"))
c=eval(input("enter a number :"))
if a==b==c:
    print(a,"it is the greatest")
else:
    n=a if a>b and a>c else b if b>c else c
    print(n,"it is the greatest")


# MATCH

# Check if number is three-digit using match
num=int(input("enter the number"))
match num:
    case n if 100<= abs(n) >=1000:
         print("it is three digit number")
    case _:
        print("not three digit number ")

# Check if number is positive, negative, or zero using match
num =num=int(input("enter the number"))
match num:
    case n if n>0:
        print("positive")
    case n if n<0:
        print('negative')
    case 0:
        print('zero')

# Menu-based options using match
print('even-odd enter 1 ')
print('positive - nonpositive enter 2 ')
print('simple interest enter 3 ')
print('root of quadratic equation enter 4 ')
n=int(input('enter the number '))
match n:
    case 1:
        n=int(input('enter the number '))
        if n%2==0:
            print('even')
        else:
            print('odd')
    case 2:
         n=int(input('enter the number '))
         if n<0:
            print('non positive')
         else:
            print('positive')
    case 3:
        p=eval("enter principle ")
        r=eval('enter rate')
        t=eval('enter time')
        print('simple interest is',(p*r*t)/100)
    case 4:
        a=eval(input("enter a number : "))
        b=eval(input("enter a number : "))
        c=eval(input("enter a number : "))
        d=b**2-4*a*c
        if d>0:
            print("Two real & distinct roots")
        elif d<0:
            print("Imaginary (complex) roots")
        else:
            print("Two real & equal roots (also called repeated or coincident roots)")

# Print message based on data type using match
n = eval(input("Enter the number: "))
match n:
    case x if type(x) is int:
        print("Monday")
    case x if type(x) is float:
        print("Tuesday")
    case x if type(x) is complex:
        print("Wednesday")
    case x if type(x) is bool:
        print("Thursday")
    case _:
        print("Other type")

# Check for specific substrings in input string
s=input('enter the string : ')
match s:
    case x if 'mysirg' in s :
        print('one')
    case x if 'education' in s:
        print('two')
    case x if 'services' in s:
        print('three')
