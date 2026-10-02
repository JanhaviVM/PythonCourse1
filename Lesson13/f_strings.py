# methods to print values on terminal


# placeholder

name = "Janhavi"
coins = 3
message = "\n%s has %s coins left" % (name, coins)
print(message)

# format with placeholder

message = "\n{} has {} coins left".format(name, coins)
print(message)

# format with index

message = "\n{1} has {0} coins left".format(coins, name)
print(message)

# format with placeholder variable names

message = "\n{name} has {coins} coins left".format(name=name, coins=coins)
print(message)

# format with dictionary

player = {"name": "Janhavi", "coins": 3}

message = "\n{name} has {coins} coins left".format(**player)
print(message)


# f-string, this is the way!
# Mandalorian reference

message = f"\n{name} has {coins} coins left"
print(message)

# f-string using expressions
message = f"\n{name} has {2 * 5} coins left"
print(message)

# f-string using method
message = f"\n{name.lower()} has {2 * 5} coins left"
print(message)

# f-string using dictionary
message = f"\n{player['name']} has {coins} coins left"
print(message)


# f-string using formatting
print("\n\nf-string using formatting")
num = 10

# the "." represents that we are formatting the value
# formatting with .2f i.e. upto two decimals fixed
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# formatting with for loop

for num in range(1, 11):
    # note, it does not print for value of 11
    print(f"2.25 times {num} is {2.25 * num:.2f}")

print("")
for num in range(1, 11):
    # note, it does not print for value of 11
    print(f"{num} divided by {num / 4.52:.2%}")
