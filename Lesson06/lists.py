# ----------

# Lists

# ----------

print("")
print("")
print("Lists")
print("")

users = ['Dave', 'John', 'Sarah']
data = ['Dave', 42, True]
emptylist = []

print("Dave" in users)
print("Dave" in data)
print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index("Sarah"))

print(users[0:2])
print(users[0:])

print(len(data))

users.append('Elsa')
print(users)

# append to list
users += ['Jason']
print(users)
# instead of above if you do below
# users += 'Jason'
# print(users)
# output when you print users will be
# ['Dave', 'John', 'Sarah', 'Elsa', 'Jason', 'J', 'a', 's', 'o', 'n', 'Robert', 'Jimmy']

users.extend(["Robert", "Jimmy"])
print(users)

# we commented this out as we don't want to mix datatypes in our list (yet)
# users.extend(data)
# print(users)

# so far we have appended or added items only to the end of the

# append at specific position syntax

# 1st way
users.insert(0, 'Bob')
print(users)

# 2nd way
# notice we added 2:2, because we dont want to replace anything

# below is also known as slice or slicing
users[2:2] = ['Eddy', 'Alex']
print(users)

# replace at a specific position syntax

# below is also known as slice or slicing list
users[1:3] = ['Robert', 'JPJ', "Anne"]
# it only replaced position from 1 to 2, and not what was at 3,
# similar to how retrieving index users[1:3] only returned John and Sarah earlier
print(users)


# removing data from list

# removing a single value
users.remove('Bob')
print(users)

# pop off last user from list

# when we use pop, it prints the user that was removed, which can be misleading
print(users.pop())
print(users)

# to delete specific user or list item
del users[0]
print(users)

# to delete list completely
# del data

# clear list
data.clear()
print(data)

# lower case

users[1:3] = ['dave']

# sorting

users.sort()
print(users)
# lower case list items come after upper case list items are sorted
# the 'dave' we added comes last! and 'Anne', 'Alex' was replaced by the lower case 'dave' still!
# since we performed the sort after the 'dave' was inserted it looks like below
# Before adding dave ['JPJ', 'Anne', 'Alex', 'John', 'Sarah', 'Elsa', 'Jason', 'Robert']
# Afte adding dave ['Alex', 'Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sarah', 'dave']

# this key=str.lower only works if the entire list is of datatype string, or rather the same datatype
users.sort(key=str.lower)
print(users)
# it tells to include the lowercase in the alphabetical  sorting
# Before Sort ['Elsa', 'JPJ', 'Jason', 'John', 'Robert', 'Sarah', 'dave']
# After Sort ['dave', 'Elsa', 'Jason', 'John', 'JPJ', 'Robert', 'Sarah']

# reversing a list
nums = [4, 42, 78, 1, 5]
print(nums)
nums.reverse()
print(nums)

# descending order
nums.sort(reverse=True)
print(nums)

# ascending order
nums.sort()
print(nums)

# here above the sort and reverse are directly changing/mutating the list
# what if we don't want to mutate the original list of nums = [4, 42, 78, 1, 5]
# for this we use global sorted approach

nums = [4, 42, 78, 1, 5]
# we are using the global sorted function to achieve sorting & reversing withtout mutating the original list
print(sorted(nums, reverse=True))
# original list remains unaffected
print(nums)


# Three different ways to make a copy of a list

print("")
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)


# we can also check the Type of list

print(type(nums))

# creating a list using constructor

mylist = list([1, "Neil", 2])
print(mylist)

# ----------

# Tuples

# ----------

print("")
print("")
print("Tuples")
print("")
# using constructor
mytuple = tuple(('Dave', 42, True))

# below is called assigning values to tuple or packing the tuple
anothertuple = (1, 4, 2, 8, 2, 2)


print(mytuple)
print(anothertuple)

print(type(mytuple))
print(type(anothertuple))
# both prints <class 'tuple'>
# whatever we learnt about lists also app;lies to tuples,
# the only difference is tuples cannot be mutated unlike lists

print(mytuple)
newlist = list(mytuple)
newlist.append('Neil')
print(newlist)

newtuple = tuple(newlist)
print(newtuple)

# we can also unpack a tuple into new variable names

print("")
print(anothertuple)
# below are variables holding the values coming from anothertuple
(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

# tuple methods

# count and index

# count the occurances of the numebr two in anothertuple
print("")
print(anothertuple)
print(anothertuple.count(2))
# o/p will be 3
