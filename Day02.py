# TYPE CONVERSION

# Convert integer to string
print(str(40))

# Get ASCII value of character
print(ord('m'))

# Get character from ASCII value
print(chr(100))

# Convert string to integer (only integral strings allowed)
print(int('10'))

# Convert integer to boolean
print(bool(46))

# Convert in into string and vice versa

print(int('10'))
print(str(10))

# BASE CONVERSION

# Print number and its binary representation
print(89,bin(89))

# Binary to decimal
a=0B1100101
print(a)

# Hexadecimal to octal
a=0x2f
print(oct(a))

# Octal number
a=0o125
print(a)

# Sum of octal and hexadecimal numbers
a=0o31
b=0x27
sum = a+b
print(bin(sum),sum)  # Print binary and decimal sum


# IMPORT FROM KEYBOARD

import math as m

# Input string
a= input("enter  your name : ")
print(a)

# Input two integers and print sum
a,b=[int(x) for x in input("enter two number : ").split()]
print("sum : ",a+b)

# Input radius and calculate area of circle
r=eval(input("enter the radius : "))
print("area : ",m.pi*r**2)

# Input number and print its square
s=eval(input("enter number for square : "))
print("square : ",s**2)

# Input character and print ASCII value
c=input("enter a character : ")
print(ord(c))


# SIMPLE CALCULATION ON USER DATA

import math as m

# Calculate simple interest
p,r,t=8,6,8
print("intrest : ",(p*r*t)/100)

# Calculate area of circle
r=2
print("area : ",m.pi*r**2)

# Input three numbers and calculate average
a,b,c=[int(x) for x in input("enter three numbers for average : ").split()]
print("average of three number",(a+b+c)/3)

# Volume of cuboid
a,b,c=2,8,10
print("volume of cuboid : ",a*b*c)

# Product of two numbers
a,b=[int(x) for x in input("enter two numbers for product : ").split()]
print("product : ",a*b)


