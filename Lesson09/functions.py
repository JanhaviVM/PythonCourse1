def hello_world():
    print("Hello World")


hello_world()

# reusable function
# using placeholders for function accepting values i.e. to pass values to functions

# parameters are in definition, argeuments are in functon call


def sum(num1, num2):
    print(num1+num2)


sum(1, 2)
sum(3, 2)
sum(100, 3)


def sum(num1, num2=3):
    if (type(num1) is not int or type(num2) is not int):
        # below is called an early return
        return
    return num1 + num2


total = sum(2, 3)
# returns 5
total = sum('a', 4)
# return None
print(total)

total = sum(1)
# throws error if default values are not specified in parameters
print(total)
# prints 4...for 1 + default value 3 in parameters


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        # below is called an early return
        # if you dont want it to return None when values are passed incorrectly,
        # then type 0 after return like below
        return 0
    return num1 + num2


total = sum(1)
print(total)


# what to do when you don't know how many arguments will be passed to the function?

# * represents n number of arguements being passed
def multiple_items(*args):
    # *args will make the data/args passed inside the function as a tuple
    print(args)
    # so we will have to work with the data as a tuple
    print(type(args))


multiple_items("Dave", "Sarah", "John")
multiple_items(1, 2, 3)

# multiple n number of arguements, but being able to refer to them with a keyword


def mult_named_items(**kwargs):
    # **kwargs will make the data/args passed inside the function as a dictionary
    print(kwargs)
    # so we will have to work with the data as a dictionary
    print(type(kwargs))


mult_named_items(first="Dave", second="Sarah", third="John")
