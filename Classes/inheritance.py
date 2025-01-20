# Topic Inheritance

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


#     def printname(self):
#         print(self.first_name, self.last_name)


# class Student(Person):
#     def __init__(self, first_name, last_name):
#         super().__init__(first_name, last_name)


# s1 = Student("Alice", "Cooper")
# s1.printname()

# Parent class
# Method overriding and Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

    def print_message(self):
        return "I am feeling good."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."


dog = Dog("Charlie")
print(dog.speak())
print(dog.print_message())

an1 = Animal("Max")
print(an1.speak())


print("==========================")

# Using super keyword
# Single Inheritance - inherits from one one parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self):
        return f"Employee name is {self.name} and salary is {self.salary}."

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


m1 = Manager("Akira", 50000, "IT")
print(m1.print_info())
print(m1.department)

print("==========================")

# Multilevel inheritance - A chain of inheritance

class Grandfather:
    def __init__(self, grandfather_name):
        self.grandfather_name = grandfather_name
        print("Constructor grandfather")

    def feature_grandfather(self):
        print("Feature from grandfather")

class Parent(Grandfather):
    def __init__(self, grandfather_name, parent_name):
        super().__init__(grandfather_name)
        self.parent_name = parent_name

        print("Constructor parent")


    def feature_parent(self):
        print("Feature from Parent")

class Child(Parent):
    def __init__(self, grandfather_name, parent_name, child_name):
        super().__init__(grandfather_name, parent_name )
        self.child_name = child_name

        print("Constructor child")

    def feature_child(self):
        print("Feature from Child")


c1 = Child("John henry", "Max", "Bruce")
print(c1.child_name)

print("===================")

# Mutiple Inheritance

class Father:
    def __init__(self, father_name):
        self.father_name = father_name
        print("Father constructor")


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
        print("Mother constructor")

class Sister:
    def __init__(self, sister_name):
        self.sister_name = sister_name
        print("Sister constructor")

# While we have mutliple inheritance then first parameter is the parent which we can call using super
class Child(Father, Mother, Sister):
    def __init__(self, father_name, mother_name, sister_name, child_name):
        super().__init__(father_name)
        Mother.__init__(self, mother_name)
        Sister.__init__(self, sister_name )

        self.child_name = child_name
        print("Child Constructor")
        print(self.father_name, self.mother_name, self.sister_name)


c1 = Child("Max", "Esha", "john", "Meera")

print("================================")


# Heirarichal Inheritance and Hybrid Inheritance

class SeperateChild:
    def feature_separate(self):
        print("separate child")

class NewParent:
    def feature_parent(self):
        print("This is Parent class")

class Child1(NewParent):
    def feature_child(self):
        print("This is Child one")

class Child2(NewParent):
    def feature_child2(self):
        print("This is Child 2")

class Child1Son(Child1):
    def feature_child1_son(self):
        print("Child 1 son")

class MutipleChild(SeperateChild, Child2):
    def mutliple_feature(self):
        print("Multiple feature child")



ch1 = Child1Son()
ch1.feature_child1_son()

m1 = MutipleChild()
m1.feature_child2()
m1.feature_separate()



