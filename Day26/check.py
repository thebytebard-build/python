#this is for checkingdemo.py
import demo

demo.module_check()

import math
#print(math.__file__) =>raise an error

print(demo.__file__)
print(__file__)

#not possible for math,__file__ becaus it is inbuilt module