
# global and local scope for variables
# below name is available to everything in this file
name = "Dave"


def greeting(firstname):
    color = "Blue"
    # global scope is accessible locally inside the function
    print(color)
    print(name)
    # if we use name instead of firstname as parameter,
    # it will print the local scope's value in both "name" print statements
    print(firstname)

# below statement will say color is not defined, since it is local
# print(color)

# to print global scope name inside a function while having parameter with same name


def greeting2(name):
    color = "Blue"
    print(color)
    print(name)
    print(globals()['name'])


greeting("John")
greeting2("Janhavi")

# global and local scope for functions

print("global and local scope for functions")

name1 = "Jan"


def another1():
    # color is global to another function's scope
    color = "Blue"

    def greeting3(name1):
        # therefore color is accessible inside here
        print(color)
        print(name1)
        # greeting is a global function
    greeting3("Davi")


another1()


# modify assignment of variable, inside a function,
# in a situation where the variable was originally defined in the global scope

name = "Dava"
count = 1
count1 = 1


def greetings4():
    # assignment of variable that shares the same name as global does not work, creates a new variable locally
    # count1 += 1 # new count variable
    # so the solution is below
    global count1
    count1 += 1
    # accessing of a variable that shares the same name as global does work, global variable gets used
    print(count)
    print(count1)


greetings4()


# case where you need to access to global variable locally

print("case where you need to access to global variable locally")

name1 = "Jan"


def another1():
    # color is global to another function's scope
    color = "Blue"

    def greeting3(name1):
        # therefore color is accessible inside here
        nonlocal color
        color = "red"
        print(color)
        print(name1)
        # greeting is a global function
    greeting3("Davi")


another1()
