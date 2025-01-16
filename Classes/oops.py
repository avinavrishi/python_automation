# Topic Object oriented programming

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
