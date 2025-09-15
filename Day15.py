# tuple 
'''
#create tuple from list
l=[1,2,3,4,5,6]
t=tuple(l)
print(t)

#reverse the python script
t=1,2,3,4,5,6
l=tuple(reversed(t))
print(l)

#create a list of tuple for word and its unicode
l=[('a',ord('a')),('b',ord('b')),('c',ord('c'))]
print(l)  

#sum of all odd numbers in tiple
t=1,2,3,4,5,6
for x in t:
    if x%2!=0:
        sum+=x
print(sum)

'''
#creat a list of tuple and tuple contain same first letter of string and this is made from a list of string
l=['radha','kala','mithi','rani','kesari','shyam','ghan','gh','ramesh']
l.sort()
l1=[l[0]]
l2=[]
ch=l[0]
i=1
while i<len(l):
    if ch[0]==l[i][0]:
        l1.append(l[i])
    else:
        l2.append(tuple(l1))
        l1.clear()
        l1.append(l[i])
    ch=l[i]
    i+=1
l2.append(tuple(l1))
print(l2)




