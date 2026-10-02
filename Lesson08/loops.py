# break

value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("Done!")

# continue
value = 1
while value <= 10:

    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))
print("Done!")

# for loop
names = ["Dave", "Sarah", "John"]

for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "Sarah":
        break
    print(x)

for x in names:
    if x == "Sarah":
        continue
    print(x)

# for loop for ranges

# range(start at 0, upto range 4 but exclude 4)
# below starts from 0
print("")
for x in range(4):
    print(x)


# range(start at 2, upto range number 4 but exclude 4)
print("")
for x in range(2, 4):
    print(x)


print("")
# range(start at 0, upto range number 100 but exclude 100, increment by 5)
for x in range(0, 101, 5):
    print(x)
else:
    print('Glad that\'s Over!')


# nested loops

names = ["Dave", "Sarah", "John"]
actions = ["codes", "eats", "sleeps"]

print(" ")
for name in names:
    for action in actions:
        print(name + " " + action + ".")

print(" ")
for action in actions:
    for name in names:
        print(name + " " + action + ".")


# Improving the rock paper scissors game wit what we learnt now!
