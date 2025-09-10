# string part 2

'''
#count alphabets
s=input('enter a string : ')
count=0
for x in s:
    if x.isalpha():
        count+=1
print(count)

#count number of uppercase and lowercase
##digit will be ignore by uppercase and lowercase function
s=input('enter a string : ')
countu=0
countl=0
for x in s:
    if x.isupper():
        countu+=1
    elif x.islower():
        countl+=1

#convert all alphabet into uppercase
s=input('enter a string : ')
output=s.upper()
print(output)

#convert all alphabet into lowercase
s=input('enter a string : ')
output=s.lower()
print(output)

#convert uppercase into lowercase and lowercase into uppercase
s=input('enter a string : ')
output=s.swapcase()
print(output)

#count all spaces
s=input('enter a string: ')
count=0
for x in s:
    if x==' ':
        count+=1
print(count)


#count digit alphabet spaces symbol
s=input('enter a string : ')
alpha=0
digit=0
symbol=0
spaces=0
for x in s:
    if x.isalpha():
        alpha+=1
    elif x.isdigit():
        digit+=1
    elif x.isspace():
        spaces+=1
    else:
        symbol+=1
print('alphabets : ',alpha)
print('digits : ',digit)
print('symbols : ',symbol)
print('spaces : ',spaces)

#reverse word of string
s=input('enter astring : ')
l=s.split()
ln=len(l)-1
output=''
while ln>=0:
    output=output+l[ln]+' '
    ln-=1
print(output)
#method 2
s=input('enter astring : ')
l=s.split()
output=' '.join(reversed(l))
print(output)

#convert all first letter of word into uppercase and rest into lowercase
s=input('enter astring : ')
output=s.title()
print(output)

#reverse the content of each word in a stirng
s=input('enter a string : ')
l=s.split()
output=''
for x in l:
    output=output+x[::-1]+' '
print(output)
#method 2
s = input('enter a string : ')
l = s.split()
output = ' '.join([x[::-1] for x in l])
print(output)

#convert camelcase into snakecase
s=input('enter a camelcase string : ')
output=''
i=0
while i<len(s):
    if i==len(s)-1:
        output=output+s[i]
    elif s[i+1].isupper():
        output=output+s[i]+'_'
    else:
        output=output+s[i]
    i+=1
output=output.lower()
print(output)

#method2
s=input('enter a string : ')
output=''
for x in s:
    if x.isupper():
        output+='_'+x.lower()
    else:
        output+=x
print(output)
'''

