# print(x)
# when we run above print statement we get the following exception
# Traceback (most recent call last):
#   File "c:\Users\admin\Python\Lesson19\exceptions.py", line 1, in <module>
#     print(x)
#           ^
# NameError: name 'x' is not defined

# Exceptions are 'raised' in python
# versus In Javascript with 'throw' Errors

# custom exceptions can also be raised


class JustNotCoolError(Exception):
    pass


x = 2
try:
    # raise Exception("I'm a custom Exception.")
    raise JustNotCoolError("This just isn't cool, man!")
    # print(x / 1)  # x/0 gives ZeroDivisionError: division by
    # if not type(x) is str:
    # TypeError is a built-in error that can be raised.
    # raise TypeError("TypeError Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("ZeroDivisionError means a number is being divided by a zero value")
except Exception as error:
    print(error)
else:
    print("No Errors")
finally:
    print("I'm going to print with or without an error!")
