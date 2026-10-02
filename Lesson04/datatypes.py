import math

# String Datatypes

# Literal Assignment

first = 'Janhavi'
last = 'Morajkar'

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# Constructor Function (another way to assign value)

pizza = str("Pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation String

print(first+" "+last)
first += "!"
print(first)

# Casting number to a string

decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple Lines
multiline = '''
I am a big fan of the 80s fashion trends too!
And its nice to see people still sporting those interests <3

~Janhavi M.
'''

print(multiline)

# Escaping Characters, tabspace, newline, adding backward slash itself

sentence = 'I\'m back at work\tHey\n\nWhere\'s this \\located?'

print(sentence)

# String Methods

print(first)
# lower() does not alter original string variable/value
print(first.lower())
print(first.upper())
print(first)

# capitalizes the first letter in every word on the multiline variable
print(multiline.title())
print(multiline.replace("nice", "great"))
# neither title() nor replace() alter original string variable/value
print(multiline)

print(len(multiline))
multiline += "                                        \n"
multiline = "      \n" + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu

title = "menu".upper()
print(title.center(20, "="))

# gives output ========MENU========

print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print("first: " + first)
print(first[1])  # second letter
print(first[-1])  # last letter
# below excludes value at -1'th position, actual string is Janhavi!
print(first[1:-1])
print(first[1:])

# Some methods return boolean data

print(first.startswith("J"))
print(first.endswith("Z"))


# Boolean Datatype

myvalue = True
# below is constructor function
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# integer type

price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type

gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# complex type (it uses j notations) and often used in electrical engineering

comp_value = 5+3j
print(type(comp_value))
# based on real and imaginary number system
# below extracts the real number
print(comp_value.real)
# below extracts imaginary number
print(comp_value.imag)

# Built-in number functions

print(abs(gpa))  # willl print the float number 3.28
print(abs(gpa * -1))  # absolute always converts to positive
print(round(gpa))  # rounds number
print(round(gpa, 1))  # rounds the decimal of the number

# Math Modules

# when you write "import math" in the code,
# it moves this line to the top of the file due to file formatter syntax

# now we use the math module imported
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Cast a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(zip_value)
print(zip_value + 1)

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
