#list part 1

'''
#sum of element present in list
l=eval(input('enter element of list : '))
sum=0
for x in l:
    sum+=x
print("sum :",sum)

#average of element present in list
l=eval(input('enter element of list : '))
sum=0
for x in l:
    sum+=x
print("average :",sum/len(l))

#square of element present in list
l=eval(input('enter element of list : '))
sum=0
l1=[]
for x in l:
    l1.append(x**2)    
print(l1)

#sort list in descending order
l=eval(input('enter element of list : '))
l.sort(reverse=True)   
print(l)

#create list with even place element of another list
l=eval(input('enter element of list : '))
l1=[]
i=0
while i<len(l):
    if i%2!=0:
        l1.append(l[i])
    i+=1
print(l1)
#method 2
l=eval(input('enter element of list : '))
l1=l[1::2]
print(l1)

#create a lsit of first n even natural number
n=int(input('enter the number : '))
l=list(range(2,n*2+1,2))
print(l)
#method
n=int(input('enter the number : '))
l=[x for x in range(2,n*2+1,2) ]
print(l)

#store fibonacci series till n number
n=int(input('enter the number : '))
l=[0,1]
for i in range(1,n-1):
    l.append(l[i]+l[i-1])
print(l)

#store first n prime into into list 
n=int(input('enter the number : '))
l=[2]
c=3
while len(l)<=n:
    for x in range(2,c):
        if c%x==0:
            break
    else:
        l.append(c) 
    c+=1     
print(l) 
#method 2 short
n=int(input('enter the number : '))
l=[2]
c=3
while len(l)<=n:
    if all(c%x!=0 for x in range(2,c)):
        l.append(c)
    c+=1     
print(l) 
  

# add two matrix each of 3*3
l=[[0,0,0],[0,0,0],[0,0,0]]
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
for x in range(3):
    for y in range(3):
            l[x][y]=l1[x][y]+l2[x][y]
for x in l:
      print(x)
      print()


#create one list that conatain positive number and one that conatain negative number from a list
#my method
l=[-1,10,32,-52,-96,65,-54]
l1=[]
l2=[]
for x in l:
    if x>=0:
        l1.append(x)
    else:
        l2.append(x)
print(l1,l2)
#short and efficient method
l=[-1,10,32,-52,-96,65,-54]
l1=[]
l2=[]
for x in l:
    l1.append(x) if x>=0 else l2.append(x)
print(l1,l2)


##str + list question


#remove all non int value from list 
l=[20,'radha',96,83,'rani',86,'pyari']
l1=[]
for x in l:
    l1.append(str(x))
l.clear()
for x in l1:
    if x.isdigit():
        l.append(int(x))
print(l)
#method 2
p=[20,'radha',96,83,'rani',86,'pyari']
q=[x for x in l if isinstance(x,int)]
print(q)


#print all distinct value with their frequency
l=[1,8,6,5,2,6,'radha',5,'radha']
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
        print(x,':',l.count(x))

#sort a list of string
l=['rat','dog']
l.sort()
print(l)

#print first repeated string in list
l=['rat','dog','apple','boy']
for x in l:
    if l.count(x)>=2:
        print(x)
        break
else:
    print('No repeated string in list')

#count string that end with s in a list
l=['rat','dogs','apple','boys']
count=0
for x in l:
    if x[-1]=='s':
        count+=1
print(count)

'''