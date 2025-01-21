# Topic Object oriented programming

# 1 - Classes and object
# 2 - Class Attributes and method/ Instance attribute
# 3 - Constructor and Destructor
# 4 - Inheritance and Access Specifier
# 5 - Operator overriding and Operator Overloading
# 6 - Polymorphism
# 7 - Encapsulation
# 8 - Abstraction
# 9 - Static Method
# 10 - Property and Getter/Setter
# 11 - Mixins
# 12 - Magic (Dunder) Methods
# 13 - Namespaces and scope
# 14 - MetaClasses
# 15 - Object oriented Design - SOLID property

# Syntax
class Person: # Blueprint
    name = "Xyz"
    subject = ["Math", "History", "Physic"]

    def __init__(self, name , age): # This invoke automatically when we create an object
        print("-------------------")
        print("Welcome")

        self.name = name
        self.age = age
    
    def print_message(self):
        print(f"{self.name} welcome to our application. Your age is {self.age}")
        for i in self.subject:
            print(i)



p1 = Person("Max", 12) # Object
# p1.print_message()

p2 = Person("Alice", 15) # Object
# p2.print_message()

# p1.print_message()

# # del p1.age
# del p1
