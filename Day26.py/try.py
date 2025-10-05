#this is for using temprature.py and list_helper.py and grades.py modulees

import temperature as t,list_helper as l,grades as g

print("convert celsius_to_fahrenheit of 25",t.celsius_to_fahrenheit(25))
print("convert fahrenheit_to_celsius",t.fahrenheit_to_celsius(77))

lis=[23,45,12,67,34,89,11]

print(f'max number from list : {l.find_max(lis)}')
print(f"min number from list : {l.find_min(lis)}")
print(f"average of number from list : {l.find_average(lis):.2f}")

print(f"grade for 86 : {g.calculate_grade(86)}")