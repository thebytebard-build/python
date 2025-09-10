#while part 2
# Print "MySirG" n times
n=int(input("enter the number : "))
i=1
while i<=n:
    print("MySirG")
    i+=1

# Print numbers from 1 to n
n=int(input("enter the number : "))
i=1
while i<=n:
    print(i)
    i+=1

# Print numbers from n down to 1
n=int(input("enter the number : "))
n
while n>=1:
    print(n)
    n-=1

# Print first n odd numbers
n=int(input("enter the number : "))
i=1
c=1
while i<=n:
    print(c)
    i+=1
    c+=2

# Print first n odd numbers in reverse
n=int(input("enter the number : "))
n=2*n-1
while n>=1:
    print(n)
    n-=2

# Print first n even numbers
n=int(input("enter the number : "))
i=2
while i<=n*2:
    print(i)
    i+=2

# Print first n even numbers in reverse
n=int(input("enter the number : "))
i=2*n
while i>=2:
    print(i)
    i-=2

# Print squares of first n natural numbers
n=int(input("enter the number : "))
i=1
while i<=n:
    print(i**2)
    i+=1

# Print cubes of first n natural numbers
n=int(input("enter the number : "))
i=1
while i<=n:
    print(i**3)
    i+=1

# Print multiplication table of n
n=int(input("enter the number : "))
i=1
while i<=10:
    print(n,'* =',i*n)
    i+=1
