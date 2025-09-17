# set part 1

'''
#check if two list have atleast one element common
l1=[1,2,3,4,5,6]
l2=[6,7,8,9]
s1=set(l1)
s2=set(l2)
if len(s1&s2)>0:
    print('yes')
else:
    print('no')

# find common elements in three list using sets
l1=[1,2,3,4,5,6]
l2=[6,7,8,9,1]
l3=[1,5,6]
s1=set(l1)
s2=set(l2)
s3=set(l3)
print(s1&s2&s3)

#create three set and find their union
s1={1,2,3}
s2={4,5,6}
s3={7,8,9}
print(s1.union(s2,s3))

#remove all eleemnt of set 
s1={1,2,3}
s1.clear()
print(s1)

#find length of set
s1={1,2,3}
print(len(s1))

#find if two sets have no common elements 
s1={1,2,3}
s2={4,5,2,6}
if len(s1&s2)>0:
    print('yes')
else:
    print('no')

#find element that are present in one set but not in other set
s1={1,2,3}
s2={4,5,2,6}
print(s1-s2)
'''
#remove all duplicate from string 
a="aabbccdd"
s=set()
s.update(a)
a=''.join(s)
print(a)


