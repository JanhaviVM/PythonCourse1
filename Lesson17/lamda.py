from functools import reduce

# a lamda function is a single expression that returns a value

# if we pass 2, it will return square of 2 for below example
# its an expression

# squared(num) = lambda num: num * num, gets reformatted to below on save by VS Code


def squared(num): return num * num

# we cannot call above function by name, its an anonymous function
# what we can do is assign lambda to a variable


print(squared(2))

# addTwo(two) = lambda num: num + 2, gets reformatted to below on save by VS Code


def addTwo(num): return num + 2


print(addTwo(12))


# example of lambda with multiple parameters

# sum = lambda a, b: a + b, gets reformatted to below on save by VS Code
def sum_total(a, b): return a + b


print(sum_total(10, 8))

# when to use lambda?
# used inside another function,
# when you need a quick function that you dont need to save for later


def funcBuilder(x):
    # returning a function lambda
    return lambda num: num + x


# passing x into funcBuilder function
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

# passing num parameter into lambda function
print(addTen(7))
print(addTwenty(7))


# What is a Higher Order Function, two possibilities

# It's a function that takes one or more functons as the arguement!

# Or It's a function that returns a function as it's result!
# technically the above funcBuilder is also a higher order function, and so are closures!

# now we wil first create a higher order function that accepts functions as parameters


# !!! higher order functions are built into python


# remember this list can be anything, tuples, etc.
numbers = [3, 7, 12, 18, 20, 21]

# lambda num: num * num passed in brackets of map() function as first arguement, the second arguement is the data.
# below map function, iterates over every item in this list, and applies the function to it.

squarednums = map(lambda num: num * num, numbers)
# And above creates a new list, well it it not exactly a list till we do below print.
print(list(squarednums))

# lambda num: num % 2 != 0

# above returns the remainder of division, here we are checking 'num' to see if it is 'odd number'

oddnums = filter(lambda num: num % 2 != 0, numbers)

print(list(oddnums))

# from functools import reduce
# above 'reduce' at its simplest it just adds everything together, but is also used for complex things
# a function that reduce accepts, needs two parameters

# first it needs an accumulator, or subtotal, second is the current which represents the current item
# lambda acc, curr: acc + curr is passed into reduce function

numbers = [1, 2, 3, 4, 5, 1]
# by passing 10, we are setting accumulator value as 10
total = reduce(lambda acc, curr: acc + curr, numbers, 10)

# so for printing total you dont need a constructor unlike map and filter function
print(total)

# sum is a built in function that achieves the same as the reduce, but we did that for redue to explain ow reduce works!
print(sum(numbers))
print(sum(numbers, 10))


# lambda acc, curr: acc + len(curr), gets passed into reduce function below
names = ['Dave Gray', 'Sarah Ito', 'John Jacob Jingleheimershmidt']

# since we are using string in reduce function,
# we need to specify that we are not concatenating them, therefore passing 0 after the names arguement.
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)

# remember, a higher order function is one that recieves function as arguement, or returns function.
