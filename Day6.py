#while part 1

# Print numbers from 1 to n
n = int(input("enter a number : "))
i = 1
while i <= n:
    print(i)
    i += 1

# Print numbers from n to 1
n = int(input("enter a number : "))
while n > 0:
    print(n)
    n -= 1

# Print numbers from start to end
start = int(input("enter a number : "))
end = int(input("enter a number : "))
while start <= end:
    print(start)
    start += 1

# Sum of 1 to 10
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print("sum is", sum)

# Product of 1 to 10
i = 1
multiply = 1
while i <= 10:
    multiply *= i
    i += 1
print("multiply is", multiply)

# Numbers from 1 to 100 divisible by 7
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1

# Numbers from 1 to 200 divisible by both 6 and 7
i = 1
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        print(i)
    i += 1

# Sum of numbers from 20 to 50 divisible by 4
i = 20
sum = 0
while i <= 50:
    if i % 4 == 0:
        print(i)
        sum += i
    i += 1
print("sum of numbers:", sum)

# Print multiplication table of n
n = eval(input('enter a number for a table : '))
i = 1
while i <= 10:
    print(n, '*', i, '=', n * i)
    i += 1

# Factorial of n
n = eval(input('enter a number for a factorial : '))
i = 1
f = 1
while i <= n:
    f *= i
    i += 1
print("factorial :", f)

# Print numbers between x and y (increasing or decreasing)
x = eval(input('enter a number : '))
y = eval(input('enter a number : '))
if x < y:
    while x <= y:
        print(x)
        x += 1
elif y < x:
    while y <= x:
        print(y)
        y += 1
else:
    print("both are same")
