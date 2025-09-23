# function part 2

#accept integer and print multiplication table upto 10 number
def table(n):
    for i in range(1,11):
        print(n,'*',i,'=',n*i)

#print if number is odd or not
def odd(n):
    if n%2!=0:
        print('True')
    print('False')

#take three integer and print the largest one
def larget_three(a,b,c):
    print(max(a,b,c))

#take integer and print if it is prime number or not
def prime(n):
    if n==1 or n==0:
        print('no')
        return
    else: 
        for i in range(2,n):
            if n%i==0:
                print('No')
                return
    print('Yes')

#take a list and print sum and average of its element
def sum_and_average(l):
    print(f"the sum and average : {sum(l)},{sum(l)//len(l)}")

#take string and and store each character's frequency ina string
def store_frequency(s):
    s2=""
    for x in s:
        if x not in s2 and x!=' ':
            s2+=x
            s2=s2+':'+str(s.count(x))+', '
    s2=s2.rstrip(', ')
    print(s2)
            

#check if string is palindrome
def palindrome(s):
    s2=s[::-1]
    print('yes') if s2==s else print('No')


store_frequency('radha rani')