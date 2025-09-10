s=input("enter the string : ")
sub=input("enter the string : ")
count=0
l=len(s)
if s.find(sub)==-1:
    print("not found")
else:
    i=-(len(sub))
    while l>i:
        i= s.find(sub,i+len(sub),l) #i+len(sub) for big string not for char 
        if i!=-1:
            print("found at position : ",i)
            count+=1
        else:
            break
print('total number of occurance : ',count)