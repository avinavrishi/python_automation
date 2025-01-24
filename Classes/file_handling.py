
# CRUD Operation
# MEAN Stack - Mongo, Express, Angular, Node 
# MERN Stack - Mongo, Express, React, Node
# Backend + Frontend + Server
# ORM - Object relational model
# OEM - Object entity model


# Open() - two parameters - 1 - Filename, 2 - mode -  Open(filename.txt)
# Types of mode:
# 1 - read - r (Default value) - read file and gives error if file does not exist.
# 2 - append - a - open file to append or update, and if file does not exist then it will create it
# 3 - Write - w - open file to write, and if file does not exist then it will create it
# 4 - Create - x- it will create the file and gives error if the same name file exits

# Additional mode
# t - text file - open(filename.txt, "rt")
# b - to handle binary file

# file = open("demo.txt", "r")
# print(file)

file = open("demo.txt")
print(file.read(2))
file.close()

f1 = open("C:\\Users\Admin\Documents\Project\demo_2.txt") 
print(f1.read(3))
f1.close()

# Open online file and read them pending
# f2 = open("http://docs.google.com/document/d/1bjRjmxFyFjwLp30xD8y-MYqKBQJ_lgK9KhRAwjgwomU/edit?tab=t.0", "rt")
# print(f2)

f2 = open("demo.txt")
print(f2.readline())
print("=====================")


# f3 = open("demo.txt")
for i in f2:
    print(i) # this is treated as string and this is actually f2.readline() method

f2.close()


f4 = open("demo.txt")
x = f4.read()

# for i in x:
#     print(i)


f4.close()


#---------------- File Writing----------------

f6 = open("demo.txt", "w")
f6.write("This file has been overwritten")
f6.close()

f5 = open("demo.txt", "a")
f5.write("\nThis is a new line we entered")
f5.close()

f7 = open("demo.txt", "w")
f7.write("This file has been overwritten")
f7.close()

# Create a new file

f9 = open("my_file.txt", "x")
f9.close()


#-------------------------- Delete file -----------------------

import os # operating system package

# Check if file exist

if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("File does not exist.")

if os.path.exists("demo"):
    os.rmdir("demo")
else:
    print("folder does not exist.")
    os.mkdir("demo") # To make directory
    f9 = open("demo/my_file.txt", "x")
    f9.close()














