# modules can be considered as small code libraries based on related features
import sys
import random as rdm
# Enum is a module inside which Enum class exists, which we are using
from enum import Enum
from math import pi
import maharashtra
from rps7 import rock_papers_scissors
print(pi)

print(rdm.choice("123"))

# the second way to to type module name rdm. and then select from the suggestions

# the third way is to refer to python documentation
# https://docs.python.org/3/py-modindex.html

print("")
print(maharashtra.capital)
maharashtra.randomfunfacts()


# how do we know what to use from module

# there's a few ways to know what is inside a module


print(dir(rdm))
# prints a list thats not very legible

for item in dir(rdm):
    print(item)


# way to know module name
# every module has one special value
# __name__

print(__name__)
# prints "main", because this is the module we are running

print(maharashtra.__name__)
# imported module gets file name

rock_papers_scissors
sys.exit()
