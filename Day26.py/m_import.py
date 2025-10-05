# in this file we will learn about multiple import
import random as r, math as m,datetime as d

#generate random number from 1 to 100
print(f'random number from 1 to 100 : {r.randint(1,100)}')

#print square root of 144
print(f'square root of 144 : {m.sqrt(144)}')

#print date time
print(f'date and time : {d.datetime.now().replace(microsecond=0)}')