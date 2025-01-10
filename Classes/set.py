# Topic Set

# Set unordered - Order are not preserved, unindexed, duplicates are not allowed and unchangeable*

my_set = set() # Empty set
my_set_2 = {"a", "b", "a", "b", 2, True, 1} # True and 1 are consider as same/ false and 0 also
print(my_set_2)

# Lenght
print(len(my_set_2))
print(type(my_set_2))

my_set_3 = set(("a", "b", "c"))

for x in my_set_3:
    print(x)

if "a" in my_set_3:
    print("Present")

l1 = list(my_set_3)
if "a" in l1:
    l1[l1.index("a")] = "z"
    my_set_3 = set(l1)

print(my_set_3)

# Add new item in set
my_set_3.add("x")
print(my_set_3)

# Add the item of two sets
my_set_2.update(my_set_3)
print(my_set_2)

# Remove from the set
my_set_2.remove("a") # It will throw error if item does not exist
my_set_2.discard("r") # It will not throw error if item does not exist
x = my_set_2.pop()
print(x)
print(my_set_2)


# Join Set Operations
# Union

set_1 = {1,2,3,10, 0}
set_2 = {2,3,4,5,10, False}
set_3 = set_1.union(set_2) # Join two sets
print(set_3)

set_4 = set_1 | set_2
print(set_4)

set_5 = set_1.union(set_2, set_3, set_4) # Union multiple sets
print(set_5)

set_6 = set_1 | set_2 | set_3 | set_4
print(set_6)

tuple_1 = (9, 10, 11)
set_7 = set_1.union(tuple_1) # Union set and tuple but cannot do with |
print(set_7)
print(type(set_7))

l1 = [44, 43, 78]
set_8 = set_1.union(l1) # Union set and list but cannot do with |
print(set_8)

# Intersection
set_12 = {2, 5, 10}
set_11 = set_1.intersection(set_2, set_12)
print(set_11)

set_13 = set_1 & set_2
print(set_13)

set_14 = set_12.intersection(tuple_1)
print(set_14)

set_1.intersection_update(set_2)
print(set_1)

# Difference
set_01 = {1,2,3,4}
set_02 = {3,4}
set_15 = set_01.difference(set_02)
print(set_15)

set_16 = set_01 - set_02
print(set_16)

set_01.difference_update(set_02)
print(set_01)

set_001 = {1,2,3,4}
set_002 = {2,3,5,6}

set_17 = set_001.symmetric_difference(set_002)
print(set_17)

set_18 = set_001 ^ set_002
print(set_18)



