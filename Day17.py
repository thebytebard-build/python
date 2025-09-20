# set part 2

'''
#print all distinct element of list
l1=[1,2,3,4,5,6,1,2,3,5,6,4]
s=set(l1)
print(s)

#creste two set of even and odd number from a given set
s={1,2,3,4,5,6,7,8,9}
s1=set()
s2=set()
for x in s:
    s1.add(x) if x%2==0 else s2.add(x)
print(s1,s2)





#you have two list one list contain names who wears black hat and another list who wears red shoes now tell how many many person wears both
l1=['dhruv','gaurav','tanishq','ujjwal']
l2=['kartik','aanuv','ujjwal','tanishq']
s1=set(l1)
s2=set(l2)
print(s1&s2)

#create a set of tuples where each tuple has two random ludo dice number that will be equal to n 
n=int(input('enter a sum : '))
s=set()
for i in range (1,7):
    for j in range(1,7):
        if i+j==n:
            s.add((i,j))
print(s)
'''


#you have a set of five players name and now create all possible players pairs(two players at atime which means pairs of twomplayers)
s1={'rahul','ahaan','tom','radha','rihana'}
s=set()
for i in s1:
    for j in s1:
        if i<j:
         s.add((i,j))
print(s)