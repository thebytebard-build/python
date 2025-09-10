# Input two numbers and print sum
a,b=[int(x) for x in input("enter two number : ").split()]
print("Sum :",a+b)

# Input two numbers and print area of rectangle
a,b=[int(x) for x in input("enter two number : ").split()]
print("Area of rectangle :",a*b)

# Input three numbers and print average
a,b,c=[int(x) for x in input("enter three number : ").split()]
print("Average :", (a+b+c)/3)

# Remove last digit
a=2534
b=a//10
print("old number : ",a,"new number : ",b)

# Get last digit
a=2089
b=2089%10
print("the last digit of {0} is {1}".format(a,b))

# Swap values without temporary variable
a,b=2,5
a=a+b
b=a-b
a=a-b
print("swapped values are : ",a,b)

# First digit of three-digit number
a=123
print("first digit : ",a//100)

# Second digit of three-digit number
a=123
print("second digit : ",a//10%10)

# Convert Fahrenheit to Celsius
f=eval(input("enter temperature in fahrenheit to convert into celcius : "))
c=(f-32)*5/9
print("Temperature in Celsius :", c)

# Calculate percentage of total marks
a,b,c,d,e=88,96,99,99,45
p=(a+b+c+d+e)/500*100
print("Percentage :",p)

# Total points in games
g=eval(input("enter the number of games played : "))
w=eval(input("number of wins : "))
l=eval(input("number of lose : "))
print("total point is ",(w*4)+(g-(w+l))*2)

# Arithmetic operations on two numbers
a,b=[int(x) for x in input("enter two numbers : ").split()]
print("Addition :",a+b)
print("Subtraction :",max(a,b)-min(a,b))
print("Multiplication :",a*b)
print("Division :",max(a,b)/min(a,b))
print("Modulus :",max(a,b)%min(a,b))

# Swap values without temporary variable
a=a+b
b=a-b
a=a-b
print("swapped values : ",a,b)

# Compound interest calculation
p=float(input("enter the principle : "))
r=float(input("enter the rate of interest (as decimal) : "))
t=float(input("enter the time : "))
a=p*(1+r)**t
Ci=a-p
print("Compound interest :",Ci)

# Area of circle
r=eval(input("enter number for area of circle : "))
print("Area of circle :",3.14*r**2)

# Comparison operations
x=5
y=3
print(x>y) # True

a=10
b=20
c=30
print(a<b and b<c) # True

p=True
q=False
print(not p or q) # False

num1=15
num2=10
print(num1==num2 or num1>num2) # True

m=8
n=6
print(m>=n and n!=m) # True

a=5
b=5
c=10
print(a<=b and b!=c) # True

num=25
print(num % 2 == 0) # False

# Check if substring exists
a= input("enter a line : ")
print('my' in a)

# Compare two strings
a= input("enter first string : ")
b= input("enter second string : ")
print(a==b)

# Chained comparison
print(5>10<5) # False

# Logical AND between strings
print("Red" and "White") # White

# Logical OR between booleans
print(True or False) # True
