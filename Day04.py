#if else part 1
# IF-ELSE

# Check if number is positive or negative
n = int(input("enter a number: "))
if n >= 0:
    print("positive")
else:
    print("negative")

# Check if character is vowel or consonant
ch = input("enter a character: ")
if ch in 'aeiouAEIOU':
    print("it is a vowel")
else:
    print("consonant")

# Check divisibility
a = int(input("enter a number: "))
b = int(input("enter a number: "))
if a % b == 0:
    print("yes")
else:
    print("no")


# IF-ELIF-ELSE

# Check if number is zero, even, or odd
n = int(input("enter a number: "))
if n == 0:
    print("it is zero")
elif n % 2 == 0:
    print("even")
else:
    print("odd")

# Check divisibility by 2 numbers but not by 8
n = int(input("enter a number: "))
if n % 2 == 0 and n % 3 == 0 and n % 8 != 0:
    print("yes")
else:
    print("No")

# Print last digit if number is not zero
n = int(input("enter a number: "))
if n != 0:
    print("last digit", n % 10)
else:
    print("it is zero")

# Check if last digit divisible by 5
n = int(input("enter a number: "))
l = n % 10
if n != 0:
    if l % 5 == 0:
        print("yes")
    else:
        print("no")
else:
    print("it is zero")

# Discount based on bill amount
n = int(input("enter the bill amount: "))
if 0 < n < 10000:
    print("No discount")
elif 10000 <= n <= 29999:
    print("you got 10% discount")
    print("your final bill is Rs", n - (n * 10 / 100))
elif 30000 <= n <= 39999:
    print("you got 20% discount")
    print("your final bill is Rs", n - (n * 20 / 100))
elif 40000 <= n <= 49999:
    print("you got 25% discount")
    print("your final bill is Rs", n - (n * 25 / 100))
else:
    print("you got 30% discount")
    print("your final bill is Rs", n - (n * 30 / 100))


# Find smallest among four numbers (nested input checks)
print("please enter all different numbers")
a = eval(input("enter first number: "))
b = eval(input("enter second number: "))
if a == b:
    print("use different number from this", a)
    b = eval(input("enter second number: "))

c = eval(input("enter third number: "))
if c == a or c == b:
    print("use different number from these", a, b)
    c = eval(input("enter third number: "))

d = eval(input("enter fourth number: "))
if d == a or d == b or d == c:
    print("use different number from these", a, b, c)
    d = eval(input("enter fourth number: "))

n = a if a < b and a < c else b if b < c else c
print("smallest number", n if n < d else d)


# FizzBuzz check
n = int(input("enter a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print("None")


# Attendance percentage check
ch = int(input("enter a class held: "))
ca = int(input("enter a class attended: "))
p = ca * 100 / ch
print("your percentage is:", p)
if p >= 75:
    print("you are allowed to sit in exam")
else:
    print("you are not allowed to sit in exam")


# Salary increment based on slab
n = int(input("enter your salary: "))
if n < 10000:
    i = n + (n * 5 / 100)
    print("incremented salary:", i)
elif n < 20000:
    i = n + (n * 10 / 100)
    print("incremented salary:", i)
elif n < 50000:
    i = n + (n * 15 / 100)
    print("incremented salary:", i)
else:
    i = n + (n * 20 / 100)
    print("incremented salary:", i)


# Find largest of three numbers
a = eval(input("enter first number: "))
b = eval(input("enter second number: "))
c = eval(input("enter third number: "))
if a == b == c:
    print("they are equal")
else:
    print(a if a > b and a > c else b if b > c else c)


# Leap year check
n = eval(input("enter the year: "))
if n % 4 == 0 and n % 100 != 0:
    print("leap year")
elif n % 400 == 0 and n % 100 == 0:
    print("leap year")
else:
    print("not leap year")


# Nested if-else to find largest number
print("Please enter all different numbers")
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
while b == a:
    print("Use a different number than", a)
    b = eval(input("Enter second number: "))

c = eval(input("Enter third number: "))
while c == a or c == b:
    print("Use a different number than", a, "and", b)
    c = eval(input("Enter third number: "))

if a > b:
    if a > c:
        print("the largest", a)
    else:
        print("the largest", c)
else:
    if b > c:
        print("the largest", b)
    else:
        print("the largest", c)


# Leap year nested check
y = int(input("enter the year: "))
if y % 100 != 0:
    if y % 4 == 0:
        print("leap year")
    else:
        print("not leap year")
else:
    if y % 400 == 0:
        print("leap year")
    else:
        print("not leap year")


# Ticket price based on age
y = int(input("enter the age: "))
if y <= 65:
    if y < 12:
        print("$5")
    else:
        print("$10")
else:
    print("$7")


# BMI calculation
h = eval(input("enter the height in meter: "))
w = eval(input("enter the weight in kilogram: "))
bmi = w / (h ** 2)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal weight")
elif bmi < 30:
    print("overweight")
else:
    print("obesity")
