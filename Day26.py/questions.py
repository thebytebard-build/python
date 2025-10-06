#python module question

#import math module use sqrt , pi value, pow
import math 
def use_math():
    print("Square root od 25 :",math.sqrt(25))
    print("Value of pi :",math.pi)
    print("2 to the power 3 :",math.pow(2,3))

#different ways of importing

#importing whole module
import math
#importing specific function
from math import sqrt
#import all function
from math import *
#import with aliasing
from math import sqrt as sq

#import random module genrate random number from 1 and 10 and picks random item from a list['apple','banana','cherry'] anfd print their result
import random
def use_random():
    print('Randome number between 1 to 10 :',random.randint(1,10))
    l=['apple','banana','cherry']
    print('random element from list :',random.choice(l))


