# recursive function
# a function calling itself
def add_one(num):

    if num >= 9:
        print("mynum")
        return num + 1

    total = num + 1
    print(total)

    # if we don't write return below, instead of 10 we get None when we print mynewtotal
    add_one(total + 1)


mynewtotal = add_one(0)
print(mynewtotal)

# None is a special value in python, its neither True not False
