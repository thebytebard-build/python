# STRING EXAMPLES FROM LECTURE
'''
#display character of string positive and negative index wise both
n=input('enter a string : ')
i=0
for x in n:
    print('The character present at positive index {} and negative index at {} is {}'.format(i,i-len(n),x))
    i+=1

#display character in both forward and backward direction with for and while loop
#a) for loop
n=input('enter a string : ')
for x in n[::-1]:
    print(x,end='')
print()
for x in n[::]:
    print(x,end='')
#b) while loop
n=input('enter a string : ')
i=0
l=len(n)
while l>i:
    print(n[i],end='')
    i+=1
print()
i=-1
while i>=-l:
    print(n[i],end='')
    i-=1

#display all places of substring with total number of occurance with or without inbuilt function
s=input('enter a string : ')
subs=input('enter a string : ')

i=0
count=0
if s.find(subs)==-1:
    print('not found')
else:
    i=-(len(subs))
    while i<len(s):
        i=s.find(subs,i+len(subs),len(s))
        if i==-1:
            break
        print("found at index :",i)
        count+=1
print('total number of occurance : ',count)
print('total number of occurance : ',s.count(subs))

# reverse the string 
#method1
s=input('enter the string ')
print(s[::-1])
#method 2
s=input('enter the string ')
i=len(s)-1
sum=''
while i>=0:
    sum=sum+s[i]
    i-=1
print(sum)
#method3
s=input('enter the string ')
news=''.join(reversed(s))
print(news)

#print words of string in reverse order
s=input('enter a string ')
l1=s.split()
l=[]
i=len(l1)-1
while i>=0:
    l.append(l1[i])
    i-=1
s=' '.join(l)
print("reversed string :",s)

#reverse the content of words
s=input('enter a string : ')
l=s.split()
n=0
l1=[]
while n<len(l):
    l1.append(l[n][::-1])
    n+=1
s=' '.join(l1)
print("reversed string :",s)

#print all odd and even position of string
s=input('enter a number : ')
n=len(s)
for x in range(0,n,2):
    print(s[x],end="")
print()
for x in range(1,n,2):
    print(s[x],end="")

#merge  character of two strings
s1=input('enter a string : ')
s2=input('enter a string : ')
i=0
j=0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1) :
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)




'''


    







