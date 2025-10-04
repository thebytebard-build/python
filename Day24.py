#lambda and variable length argument and map,reduce,filter

#lambda

#check if number is even
s=lambda n: True if n%2==0 else False

#nth term of fibonacci series
fib= lambda n: n if n<=1 else fib(n-1)+fib(n-2)

#area of circle
area=lambda r: 3.14*r**2

#find hcf of two given number
hcf= lambda a,b: min(a,b) if  max(a,b)%min(a,b)==0 else hcf(max(a,b)%min(a,b),min(a,b))

#find words in a given string
words=lambda s: len(s.split())

#map , reduce, filter

#count the number of vowel in string using map function
s='aeiouwwaeiou'
count=sum(map(lambda x: 1 if x.lower() in 'aeiou'else 0,s))   
   

#find legth of each element in tuple with map 
t=(14,963,45698,4155)
l=list(map(lambda x : len(str(x)),t))


#create a list of number greater than given number n in set of numbers
numbers = {1, 2, 2, 3, 4}
n=2
l=list(filter(lambda x:True if x>n else False,numbers))

#filter out only int value from list
l=[4,'ff',5,'@',889,96]
inte=list(filter(lambda x: x if isinstance(x,int) else False,l ))


#find hcf of element of list
from functools import reduce
h=lambda x,y: x if y%x==0 else h(y%x,y)
l=[8,6,24]
hcf=reduce(h,l)
print(hcf)