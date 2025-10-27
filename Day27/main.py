import calculator.add  as a,calculator.division as d,calculator.multiply as m,calculator.sub as s

print(a.addition(10,2))
print(d.div(10,3))
print(m.mul(10,2))
print(s.subtraction(10,2))

from shapes import c,t,r

print(c(2))
print(r(10,2))
print(t(2,6))

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.sin(25))

import libra.books,libra.members,libra.transations

libra.books.list_books()
libra.members.list_members()
libra.transations.borrow_book(101,1)
libra.transations.borrow_book(102,3)
libra.transations.show_transactions()

from text_utils.capitalize import cap
from text_utils.count_v import c_v
from text_utils.reverse import rev

print(rev('abcde'))
print(c_v('abcde'))
print(cap('abcde'))

from temperature_c import *


print(celsius_to_fahrenheit(25))
print(kelvin_to_fahrenheit(300))
print(fahrenheit_to_celsius(77))


#here we are importing myapp
import myapp.databas.operation.create
from myapp.databas.operation import update
#myapp.databas.operation.create.c()
update.update()
