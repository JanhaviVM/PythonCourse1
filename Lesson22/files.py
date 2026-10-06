# r = Read
# a = Append (same thing as update)
# w = Write
# x = Create

import os

# above is similar to crud
# later we will learn how to delete files

# Read - error if it dosen't exist.

# read text file - rt or r, read binary file - rb
# f = open("names.txt", "rt")

# f = open("names.txt")
# read the full file
# print(f.read())
# read the first 4 characters of the file
# print(f.read(4))
# read the first line of the file

# stacking the below commands does not cause first and second line to be printed instead of printing the first one twice
# print(f.readline())
# print(f.readline())

# loop through
# for line in f:
#     print(line)

# after the file has been opened it needs to be closed, why?
# if you change somehting in file, change does not show up if the file remains open in the code.
# f.close()


# now we will try to open a file that does not exist,
# so first to avoid an error we do try block

# try:
#     f = open("name_list.txt")
#     print(f.read())
# except:
#     print("The file you wanted to read does not exist.")
# finally:
#     f.close()


# Appending the files, adding two files
# f = open("names.txt",  "a")
# f.write("\nNeil")
# f.close()

# f = open("names.txt", "r")
# print(f.read())
# f.close()


# Overwriting whats in the file
# f = open("context.txt", "w")
# f.write("I deleted all of the context")
# f.close()

# f = open("context.txt")
# print(f.read())
# f.close()


# Two ways to create a new file

# First, way. Opens a file for writing, creates the file if it does not exist

# f = open("names_list.txt", "w")
# f.close()

# Second way to create a file will also cause an error if the file exists

# try:
#     if not os.path.exists("janhavi.txt"):
#         f = open("janhavi.txt", "x")
#         f.close()
#     raise Exception
# except:
#     print("File already exists!")
# finally:
#     print("Done")


# Deleting files

# avoid an error if it dosen't exist

# if os.path.exists("janhavi.txt"):
#     os.remove("janhavi.txt")
# else:
#     print("The file you wish to delete does not exist")

# IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!
# implicit exception handling for files also exists!


# below we will copy content of one file to another iin a different way

with open("morenames.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
