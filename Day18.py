# dict part 1

'''
#create a dict where first n natural numbers are keys and their squares are values
n=int(input('enter the first n number : '))
d={x: x*x for x in range(1,n+1)}
print(d)


#sort a dictionary by its key
d={'c':3,'a':1,'d':4,'b':2}
d2={}
for k,v in reversed(sorted(d.items())):
    d2[k]=v
print(d2)

#create a dictionary where each key is cricketrs names and data values are tuples of 4 element - matches played,total runs,half centuries and centuries
d={}
for i in range(5):
    name=input('enter a name : ')
    t=eval(input('enter the record : '))
    d[name]=t
print(d)

#find the maximum size batch code , a dictionary whose keys are batch code and values are batch size
batches = {"B101": 45,"B102": 60, "B103": 38,  "B104": 75,"B105": 50}
for k,v in batches.items():
    if v==max(batches.values()):
        print(f"{k} : {v}")
'''

#create a dict object where eaach key is first letter of city and values are city name from list
cities = ["Delhi", "Paris", "Tokyo", "Sydney", "New York"]
d={x[0]:x for x in cities}
print(d)