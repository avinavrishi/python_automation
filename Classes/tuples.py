# Topic Tuples

# Tuple is a colletion which is ordered and unchangeable, or immutable
# Duplicate values are allowed.

list1 = [1,2,3,4]

tuple1 = ("apple", 1 , 2)
print(len(tuple1))

print(type(tuple1))

tuple3 = (1) # Not a tuple
tuple2 = (1,) # Is a tuple
print(type(tuple2))

list1[0] = 20
print(list1)

# Access the element of the tuples
print(tuple1[0])
print(tuple1[:-1])

if "apple" in tuple1:
    print("Present")

# If we want to change the element then we need to convert the tuple into list
# Same goes for adding new element
y = list(tuple1)
y[1] = "grapes"
tuple1 = tuple(y)
print(tuple1)

tuplex = ("orange",)
tuple1 +=tuplex # Joining two tuples
print(tuple1)

# del tuple1 # We can delete the whole object but not the elements

# Unpacking the tuples
(a,*b) = tuple1
print(a)
print(b) # using * we can assign the values in the variable as a list
print(type(b))

(*x, y, z) = tuple1
print(x)
print(y)
print(z)

# loop Through a tuples
for i in tuple1:
    print(i)
print("++++++++++++++++")

for i in range(len(tuple1)):
    print(tuple1[i])

print("================")

i = 0
while i < len(tuple1):
    print(tuple1[i])
    i +=1

print("================")

x = tuple1 * 2 + tuple1 * 5
print(x)

print(x.count("apple"))

print(x[1:].index("apple"))
