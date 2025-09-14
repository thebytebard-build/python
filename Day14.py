#list part 2

'''
#revrse the list
l=[1,2,3,4,5,6]
l.reverse()
print(l)

#print even number
l=[1,2,3,4,5,6]
for x in l:
    if x%2==0:
        print(x)

#print odd number
l=[1,2,3,4,5,6]
for x in l:
    if x%2!=0:
        print(x)  

#print even place number
l=[11,85,63,45,85,56]
i=0
while i<len(l):
    if i%2==0:
        print(l[i])
    i+=1   

#print sum of all element in list
l=[1,2,3,4]
sum=0
for x in l:
    sum+=x
print(sum)  

#count even number
l=[1,2,3,4,5,6]
count=0
for x in l:
    if x%2==0:
        count+=1
print(count) 

#count number which is both divisible by 2 and 5
l=[1,2,3,4,5,6,55,10,90]
count=0
for x in l:
    if x%2==0 and x%5==0:
        count+=1
print(count) 

#sum of even number
l=[1,2,3,4,5,6]
sum=0
for x in l:
    if x%2==0:
        sum+=x
print(sum)

#count even number
l=[1,12,24,30,58]
count=0
for x in l:
    if x%3==0 and x%4==0:
        count+=1
print(count)

#print positive and begative values
l=[1,2,5,6,-5,8,-6]
c_p=0
c_n=0
for x in l:
    if x>=0:
        c_p+=1
    else:
        c_n+=1
print('negative :',c_n,'positive :',c_p)

#print the largest number in list
li=[1,2,5,6,-5,8,-6]
l=0
for x in li:
    if l<x:
        l=x
print(l)

#ask user for leength of string then input
n=int(input('enter the length of list : '))
l=[]
for x in range(n):
    l.append(int(input('enter the element : ')))
print(l)

#ask user a new and old number if that number exist in list then change old number with new number
l=eval(input('enter a list : '))
on=eval(input('enter old number : '))
nn=eval(input('enter new number : '))
if on in l:
    l[l.index(on)]=nn
print(l)

#remove all even number from list 
n=[1,2,3,4,5,6]
l=[x for x in n if x%2!=0]
print(l)
#method 2
n=[1,2,3,4,5,6]
for x in n:
    if x%2==0:
        n.remove(x)
print(n)

#ask user a number then remove all the element that can be divided by number
l=[2,4,3,6,4,8,5,10,6,12]
n=eval(input('enter a number : '))
l1=[x for x in l if x%n!=0]
print(l1)

#put odd and even number from l into odd and even list
l=[1,2,3,4,5,6,7,8,9,10]
odd=[]
even=[]
for x in l:
    even.append(x) if x%2==0 else odd.append(x)
print(odd)
print(even)  

#create tww list of random number then mergeboth list
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l=l1+l2
print(l)

#remove all duplicate  values
l=[1,2,3,'radha',8,'radhaa']
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l)

#ask for number if that number exist in list then print t-else print -1
l=[1,2,3,5,8,63]
n=eval(input('enter a nuber : '))
if n in l:
    print(l.index(n))
else:
    print('-1')

#enter the 10 input in list and store the revrse of list in another list
l=[1,2,3,4,5,6,7,8,9,10]
l.reverse()
l2=l.copy()
print(l2)

#average of elemnt of list present in list
l=[10,20,30]
sum=0
for x in l:
    sum+=x
print(sum/len(l))

#find the word which has the most frequency
l=[1,2,3,1,2,3,4,5,2,6,8,1]
value=0
c=0
for x in l:
    if l.count(x)>=c:
        value=x
        c=l.count(x)
li=[value]
for x in l:
    if l.count(x)==c:
        if x not in li:
           li.append(x)
print(li,'=',c)

#create a list that have same element present in two list
l1=[1,2,3,7,8,9]
l2=[1,2,3,4,5,6,7,8,9]
l=[]
for x in l1:
    if x in l2:
        l.append(x)
print(l)

#find second largest number without sorting
l=[1,5,9,3,5,8]
v=max(l)
while True:
    if v in l:
        l.remove(v)
    else:
        break
print(max(l))

#take a list from use and print print product of all values
l=eval(input('enter the list element : '))
multi=1
for x in l:
    multi*=x
print(multi)

#print all prime number present in list
l=[1,2,11,55,36,23,51]
for x in l:
    for j in range(2,x):
        if x%j==0:
            break
    else:
        if x!=1:
           print(x)

#split a list into two halves
l=[1,2,11,55,36,23,51]
l1=[]
l2=[]
for x in l:
    l1.append(x) if len(l1)<len(l)//2 else l2.append(x)
print(l1,l2)

#swap first lement to the last element
l=[1,2,11,55,36,23,51]
a=l[0]
l[0]=l[-1]
l[-1]=a
print(l)

#generate squares upto n in list
n=int (input('enter a number : '))
l=[]
for x in range(1,n+1):
    l.append(x**2)
print(l)

#count the string and put into another list
l=['radha','apple','ram','kela']
l1=[]
for x in l:
    l1.append(len(x))
print(l1)

#generate a string where each elemenet repeat itself three times
l=['a','b','c']
l1=[]
for x in l:
    l1.append(x*3)
print(l1)

#print odd number with odd and even numeber with even in list
l=[21,36,88,15,16,96,87]
l1=[]
s1='EVEN'
s2='ODD'
for x in l:
    l1.append([s1,x]) if x%2==0 else  l1.append([s2,x])
print(l1)

#rverse list using slicing
l=[1,2,3,4,5,6]
l1=l[::-1]
print(l1)

#print all third index element using slicing
l=[1,2,3,4,5,6]
l1=l[2::3]
print(l1)

#split a list into two halves 
l=[1,2,3,4,5,6]
l1=l[:len(l)//2]
l2=l[len(l)//2::]
print(l1,l2)

#print last n elemnt of list
l=[1,2,3,4,5,6]
n=int(input('enter a number : '))
l1=l[len(l)-n:]
print(l1)

#print last n elemnt of list revserse
l=[1,2,3,4,5,6]
n=int(input('enter a number : '))
l1=l[-1:-(n+1):-1]
print(l1)

#print from start and end index and ask user these start and end from user
l=[1,2,3,4,5,6]
s=int(input('enter start index : '))
e=int(input('enter start index : '))
l1=l[s:e+1]
print(l1)

#print form starting n number in reverse order
l=[1,2,3,4,5,6]
n=int(input('enter the index : '))
l1=l[n-1::-1]
print(l1)
'''





    





