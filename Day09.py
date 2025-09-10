#pattern

# Square star pattern: prints a square of '*' of size n
n=eval(input("enter a number :"))
for i in range (n):
    for j in range(n):
        print('*',end=' ')
    print()

# Square number pattern: prints numbers 1 to n in each row
n=eval(input("enter a number :"))
for i in range (n):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

# Square opposite number pattern: prints numbers n to 1 in each row
n=eval(input("enter a number :"))
for i in range (n):
    for j in range(n,0,-1):
        print(j,end=' ')
    print()

# Square vertical number pattern: prints the same number in each row (1 to n)
n=eval(input("enter a number :"))
for i in range(1,n+1):
    for j in range(n): 
        print(i,end=' ')
    print()

# Square vertical opposite number pattern: prints the same number in each row (n to 1)
n=eval(input("enter a number :"))
for i in range(n,0,-1):
    for j in range(n):
        print(i,end=' ')
    print()

# Left-aligned triangle number pattern: numbers increase from 1 to row number
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

# Left-aligned triangle vertical number pattern: prints same number in each row
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print()

# Left-aligned triangle opposite number pattern: numbers decrease from row number to 1
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

# Left-aligned triangle opposite number vertical pattern: prints decreasing numbers from n
n=5
for i in range(1,n+1):
    for j in range(i):
        print(n-j,end=' ')
    print()

# Left-aligned triangle opposite number vertical pattern: prints same number in each row (n-i+1)
n=5
for i in range(1,n+1):
    for j in range(i):
        print(n-(i-1),end=' ')
    print()

# Left-aligned triangle star pattern: prints '*' in increasing order per row
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()

# Vertical opposite number pattern: prints decreasing numbers per row from n to i+1
n=5
for i in range(n):
    for j in range(n,i,-1):
        print(j,end=' ')
    print()

# Left-aligned triangle downward vertical number pattern: prints same number per row
n=5
for i in range(n):
    for j in range(n,i,-1):
        print(n-i,end=' ')
    print()

# Left-aligned triangle downward star pattern: prints '*' in decreasing order per row
n=5
for i in range(n):
    for j in range(n,i,-1):
        print('*',end=' ')
    print()

# Left-aligned triangle downward opposite number pattern: numbers decrease per row
n=5
for i in range(n):
    for j in range(n,i,-1):
        print(j-i,end=' ')
    print()

# Increasing number triangle pattern: prints consecutive numbers across rows
n=5
t=1
for i in range(n):
    for j in range(i+1):
        print(t,end=' ')
        t+=1
    print()

# Same increasing number triangle pattern (formula approach)
print("printing same pattern again with different solving way")
n = 5
for i in range(n):
    for j in range(i+1):
        print((i*(i+1))//2 + j + 1, end=' ')
    print()

# Left-aligned opposite number triangle pattern: numbers decrease from row length
n=5
for i in range(n):
    for j in range(i+1,0,-1):
        print(j,end=' ')
    print()

# Right-aligned right-angle star pattern
n=5
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()

# Right-aligned right-angle number pattern: prints 1 to row number
n=5
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(1,i+2):
        print(k,end=' ')
    print()

# Right-aligned right-angle vertical number pattern: prints row number repeatedly
n=5
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(i+1):
        print(i+1,end=' ')
    print()

# Right-aligned right-angle star pattern with double spacing
n=5
for i in range(n):
    for j in range(n-(i+1),0,-1):
        print(' ',end=' ')
    for k in range(i+1):
        print('*  ',end=' ')
    print()

# Diamond star pattern
n=5
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(i+1):
        print('*  ',end=' ')
    print()   
n=n-1
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(n-i):
        print('*  ',end=' ')
    print()   

# Opposite triangle star pattern (upside down)
n=5
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*  ',end=' ')
    print()  

# Same opposite star pattern repeated
n=5
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*  ',end=' ')
    print() 
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(i+1):
        print('*  ',end=' ')
    print()   
