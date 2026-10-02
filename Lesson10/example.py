# while loops and how they evaluate true and false conditions

value = True
while value:
    print(value)
    value = False

value = True
while value:
    print(value)
    value = 0

value = "y"
while value:
    print(value)
    value = 0

# with below example, the loop evaluates when we use continue keyword
value = "y"
count = 0
while value:
    count += 1
    print(count)

    if (count == 5):
        break
    else:
        value = 0
        continue
