# dict part 2

'''
#ask the user to enter n number of subject and its marks and sotored it in dictionary 
d={}
n=int(input('enter the number of students : '))
for i in range(n):
    name=input('enter subject name : ')
    marks=int(input('enter subject marks : '))
    d[name]=marks
print(d)

#there are two list one contain word of numers and another cotain numeric digit now make it dictionary
l1=['ten','twienty','thirty','forty','fifty']
l2=[10,20,30,40,50]
d={}
i=0
while len(l1)>i:
    d[l1[i]]=l2[i]
    i+=1
print(d)

# sum of all the values in dictonary
d={'a':1,'b':2,'c':3,'d':4}
print(sum(d.values()))

#product of all the values in dictonary
d={'a':1,'b':2,'c':3,'d':4}
m=1
for x in d.values():
    m*=x
print(m)

#create a dictionay where each key is word and its value is frequency
d={}
s=input('enter the string : ')
for x in s:
    d[x]=d.get(x,0)+1
print(d)

#store name as key and their list of 5 marks in dictionary and print sum and theirr percentage
d={}
s=[]
p=[]
for x in range(5):
    name=input('enter a name : ')
    marks=eval(input('enter the list : '))
    d[name]=marks
for x in d.values():
    s.append(sum(x))
    p.append(sum(x)/5)
for x in range(5):
    print(f"sum : {s[x]} and percentage : {p[x]}")

#store marks of five subject and their marks
d={'math':100,'biology':96,'chemistry':99,'accounts':100,'english':100}
name=input('enter the subject : ')
if name.lower() in d:
    print(d[name.lower()])
else:
    print('invalid')


#store five student name as key and list of marks as value then find which student have highst marks
d={
    "Rahul": [80, 75, 90, 88, 70], 
    "Amit": [70, 85, 60, 75, 80],
    "Sneha": [95, 88, 92, 90, 85],
    "Rohan": [65, 70, 60, 68, 72],
    "Priya": [90, 85, 80, 92, 88]
}

l=[0,0]
for k,v in d.items():
    if l[1]<sum(v):
        l[0]=k
        l[1]=sum(v)
print(f"the highest marks of student {l[0]} : {l[1]} ")
'''

#two dictionary whose keys are string and value are  number merge both of them if they have same key then add their value
d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
d3=d1.copy()
for k,v in d2.items():
    if k in d3:
        d3[k]+=v
    else:
        d3[k]=v
print(d3)



















    




