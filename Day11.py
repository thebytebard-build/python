'''
# check if string has only alphabet
s=input('enter a string : ')
if s.isalpha():
    print("yes")
else:
    print("no")

#check if a given character present in string or not
s=input('enter a string : ')
ch=input('enter a string : ')
if ch in s:
    print("yes")
else:
    print('no')

#count vowels in a string
#method1
s=input('enter a string : ')
vowels='aeiouAEIOU'
i=0
for x in vowels:
    if s.count(x)>0:
        i=i+s.count(x)
print('number of vowels : ',i)
#method 2
s=input('enter a string : ')
vowels='aeiouAEIOU'
i=0
for x in s:
    if x in vowels:
        i=+1
print('number of vowels : ',i)

#count vowels in a string
#method 1
s=input('enter a string : ')
count=s.count(' ')
print('number of words : ',count+1)
#method 2
s=input('enter a string : ')
l=s.split()
print('number of words : ',len(l))

#reverse the string
#method 1
s=input('enter a string : ')
rs=''.join(reversed(s))
print('reversed string : ',rs)
#method 2 with slice operator and indexing

#revrse the word of a string
s=input('enter a string : ')
l=s.split()
ln=len(l)-1
l1=[]
while 0<=ln:
    l1.append(l[ln])
    ln-=1
rs=' '.join(l1)
print(rs)

#extract digits from string and store in a list 
s=input('enter a string : ')
l=[]
for x in s:
    if x.isdigit():
        l.append(x)
print(l)

#check if a number is pallindrome
s=input('enter a string : ')
rs=''.join(reversed(s))
if rs==s:
    print("yes")
else:
    print('no')

#convert a string into uppercase
s=input('enter a string : ')
us=s.upper()
print('uppercase string : ',us)

# find maximum length of word in a string
#method1
s=input('enter a string :')
l=s.split()
maxl=0
maxw=''
for x in l:
    if maxl<len(x):
        maxl=len(x)
        maxw=x
    elif maxl==len(x):
        maxw=maxw+','+x
print(maxw,maxl)
#method 2
s = input('enter a string : ')
words = s.split()
max_len = max(len(w) for w in words)       
max_words = [w for w in words if len(w) == max_len]  
print("Longest word(s):", ", ".join(max_words))
print("Length:", max_len)

#mix of list and str

#remove all no int value from list
l=input('enter a string : ').split()
s=''.join(l)
l.clear()
i=0
digits='1234567890'
for x in s:
    if x not in digits:
        l.append(x)
print(l)

'''



  







