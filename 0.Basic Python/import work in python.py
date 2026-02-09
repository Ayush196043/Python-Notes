# Import work in python. 

import math
result=math.sqrt(9)
print(result) # Output:-3.0

# 1.From keyword--> use kar ke module ke spasfic function ka use karsakate hai.

from math import sqrt,pi #use as function.

result = sqrt(9) * pi
print(result)

#2. as keyword --> use kar ke kisi module or uske function ko short form me convert kar sakete hai

import calendar as c

print(c.month_name[2])
print(c.day_name[0])
print(14)

#3. dir function --> jis module ke bare me nahi pata ho use janane ke liye dir(module_nmae) function use karte hai
import calendar as c
print(dir(c))
print(c.APRIL,type(c.APRIL))

#4.import eyerythings.
#from math import *

# you are make your one module.

















