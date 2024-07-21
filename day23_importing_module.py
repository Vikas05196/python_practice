#module
#module contains set of functions which will be used by importing them 

#generic import

# import random

# print(random.randint(1,10))

# #function import

from  random import randint

print(randint(100,200))

#universal import 

from random import *

print(random())

print("mpg")
random_a = randint(10,25)
random_b = randint(200,400 )

mpg = random_b//random_a

print(mpg)