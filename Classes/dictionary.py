#Topic Dictionary

# We store and (key : value) pair.
# Properties - ordered* , changeable, and do not allow duplicates

my_dict = dict()

my_dict_01= {} # this is to declare empty dictionary not set

print(type(my_dict_01))

my_dict_1 = {
    "brand" : "Ford",
    "model": "Mustang",
    "year": 1969,
    "color": ["black", "white"],
}

print(my_dict_1)

my_dict_2 = {
    "brand" : "Ford",
    "model": "Mustang",
    "year": 1969,
    "color": ["black", "white"],
    "year": 1888,
    1999: "year"
}

print(my_dict_2) # Duplicates are not allowed it will maintain the latest updated element

print(len(my_dict_1))

# Access item

print(my_dict_1["brand"]) # it will give error if key is not present (keyerror)

data = my_dict_1.get("name", "Not present") # To check whether key present in the dictionary if not return the default/given value
print(data)

# Get keys

my_keys = my_dict_1.keys()
print(type(my_keys))
print(my_keys)

for i in my_keys:
    print(i)


my_dict_1["transmission"] = "Automatic"

print(my_keys) # Automatic key updates without

# Get Values
my_values = my_dict_1.values()
print(my_values)

# Get item
my_item = my_dict_1.items()
print(my_item)

if "model" in my_dict_1:
    print("present")

# Update the values
my_dict_1["model"] = "figo"
print(my_dict_1)

my_dict_1.update({"year" : 1880, "color" : "Red", "Airbag": True})
print(my_dict_1)

# Remove item
item = my_dict_1.popitem() # pop Last added element 
print(my_dict_1)
print(item)

my_item = my_dict_1.pop("model", []) # pop values with the help of key but always give a default value
print(my_dict_1)
print(my_item)

del my_dict_1["color"]
print(my_dict_1)

# my_dict_1.clear()
# print(my_dict_1)


print("================")
# looping in the dictionary

for i in my_dict_1:
    print(i, my_dict_1[i])

print("================")

for item in my_dict_1.items():
    print(item[0], item[1])

print("================")

for key, value in my_dict_1.items():
    print(key, value)


for item in my_dict_1.values():
    print(item)


# Copy the dictionary
new_dict = my_dict_1.copy()
print(new_dict)

new_dict_1 = dict(my_dict_1)
print(new_dict_1)

# Nested dictionary
my_family = {
    "child1": {
        "name": "sonu",
        "age": 12
    },

    "child2": {
        "name": "Monu",
        "age": 14
    }
}

print(my_family)

child_1 = {
    "name": "Sonu"
}

child_2 = {
    "name": "Monu"
}
my_family_1 = {
    "child_1": child_1,
    "child_2": child_2
}

print(my_family_1["child_1"]["name"])


for key, value in my_family.items():
    for x, y in value.items():
        print(x, y)