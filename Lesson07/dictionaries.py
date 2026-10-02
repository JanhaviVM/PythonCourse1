# ----------

# Dictionaries

# ----------

# Dictionaries are used to store data values that are in key value pairs

# they way lists look like JS arrays, dictionaries look like JS Objects

band = {
    "vocals": "Plant",
    "guitar": "Page"
    # pairs of key:value
}

# dictionaries can have any data type as the value within them, not just strings

# non constructor declaration
band2 = dict(
    vocals="Plant", guitar="Page"
)

print(band)
print(band2)

print(type(band))
print(type(band2))

print(len(band))
print(len(band2))


# Accessing dictionary items

# accessing the value by passing the key
print(band["vocals"])

# accessing value using get method
print(band.get("guitar"))

# list all keys

print(band.keys())

# list all values

print(band.values())

# list of key:value pairs as tuples

print(band.items())

# verify if key exists in a dictionary
print("guitar" in band)
print("triangle" in band)


# change values of dictionary

band["vocals"] = "Coverdale"
print(band)

# add new key : value pair to dictionary

band.update({"bass": "JPJ"})
print(band)

# removing items from dictionary

print("")
print(band.pop("bass"))
# we dont get tuple or key:value pair, instead we see the value that was removed
print(band)

# adding value to band directly
print("")
band["drums"] = "Bonham"
print(band)

# remove the last thing that was added
print("")
print(band.popitem())  # return a tuple
print(band)

# delete or clear items in dictionary

print("")

band["drums"] = "Bonham"
print(band)
del band["drums"]

print(band)

# clearing a dictionary

band2.clear()
print(band2)
# prints {}

# delete dictionary

del band2

# copying dictionary

# first lets know how NOT to copy dictionaries!

# below creates a reference and not a copy,
# points to the same dictionary when we do below
band2 = band
print("Bad Copy!")

print(band)
print(band2)

band["drums"] = "Dave"

print("changes points to the same reference/location in memory")
print(band)
print(band2)

# correct way to copy a dictionary

band2 = band.copy()
print("Good Copy!")

print(band)
print(band2)
print(band.popitem())
print("changes donot point to the same reference/location in memory, the two dictionaries are separate")
print(band)
print(band2)


# another way to create a copy is using the constructor function
# using the dict() constructor to creating copy of dictionary

band3 = dict(band)
print("Good copy way of dictionary!")
print(band3)


# Nested Dictionary

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)

# a dictionary can be more than 2 levels deep, in that case,
# the below syntax will extend similarly [] [] [] type of way
print(band["member1"]["name"])


# ----------

# Sets

# ----------


nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums2))

# Top advantages of a set

# no duplicates allowed

nums = {
    1, 2, 2, 3
}

print(nums)

# True is a dupe of 1, False is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}

print(nums)
# {False, 1, 2, 3, 4
# why above? well since it detected False first,
# it ignored 0 from list. same with True

# check if value in set
print(2 in nums)

# but you cannot refer to an element in set with an index position or a key


# Adding a new value to a set

nums.add(8)
print(nums)
# gives {False, 1, 2, 3, 4, 8}

# can add elements from one set to another

morenums = {5, 6, 7}

nums.update(morenums)
print(nums)
# set automatically arranges elements in ascending order

# you can use update with lists, tuples, and dictionaries too.
# whatit means is
# you dont have to pass in a set into the update function,
# to update set, it can be any of the above (lists, tuples, dictionaries)


# to merge sets, and create a new set from those

one = {1, 2, 3}
two = {5, 6, 7}

# below does not change original sets
mynewset = one.union(two)
print(mynewset)

# Keep only duplicates,
# note this mutates the original set on which intersection is being performed
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
# note this mutates the original set on which the symmetric difference update is being performed on

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
