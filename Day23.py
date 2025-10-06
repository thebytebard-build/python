# recursion questions part 1
print('roshani ........')
#print first n natural number
def nn(n):
    if n>1:
        nn(n-1)
    print(n)

#print first n natural number in reverse order
def reverse_nn(n):
    print(n)
    if n>1:
        reverse_nn(n-1)

#print first n natural odd number
def odd(n):
    if n>1:
        odd(n-1)
    print(n*2-1)

#print first n reverse odd number  
def reverse_o(n):
    print(2*n-1)
    if n>1:
        reverse_o(n-1)     

#print durgasoft n tiems
def pri(n):
    print("durgasoft")
    if n>1:
        pri(n-1)

#print first n even number
def even(n):
    if n>1:
        even(n-1)
    print(2*n)
    
#print first n reverse even number
def reverse_even(n):
    print(2*n)
    if n>1:
        reverse_even(n-1)
   
# print n square numbers
def ns(n):
    if n==1:
        print(n**2) 
        return 1
    else:
        ns(n-1)
    print(n**2) 

#print n cube numbers
def nc(n):
    if n>1:
        nc(n-1)
    print(n**3)

#print the revserse of given number
def reverse_digit(n):
    if n>0:
        print(n%10,end='')
        reverse_digit(n//10)
   
#print sum of first n natural number
def sum_n(n):
    if n>1:
       return n+sum_n(n-1)
    return 1

#print sum of first n odd number
def sum_o(n):
    if n>1:
        return 2*n-1+sum_o(n-1)
    return 1

#print sum of first n even number
def sum_e(n):
    if n>1:
        return n*2+sum_e(n-1)
    return 2


#print sum of first n square number
def sum_s(n):
    if n>1:
        return n**2+sum_s(n-1)
    return 1

#print sum of first n cube number
def sum_s(n):
    if n>1:
        return n**3+sum_s(n-1)
    return 1

#print sum of digit of given number
def sum_d(n):
    if n>0:
        return n%10+sum_d(n//10)

#print factorial of a given number
def fact(n):
    if n>0:
        return n*fact(n-1)
    return 1

#print the binary of a guven number
def bina(n):
    if n>1:
        bina(n//2)
    print(n%2,end='')

#print octal of a given decimal number
def octa(n):
    if n>1:
        octa(n//8)
    print(n%8,end='')

#print the sum of first n prime number
def sum_p(n):
   if n<2:
       return 0
   elif n==2:
       return 2
   else :
       for j in range(2,n):
           if n%j==0:
               break
       else:
           return n+sum_p(n-1)
       return sum_p(n-1)

