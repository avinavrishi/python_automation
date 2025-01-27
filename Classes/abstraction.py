from abc import ABC, abstractmethod

# - Only subclass will be instatiated.

class Animal(ABC):

    # Base class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "bark"
    
class Cat(Animal):
    def sound(self):
        return "meow"


c1 = Cat()
print(c1.sound())

# a1 = Animal()

# Static method
#--- 
class MathsOperation:

    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def substract(a,b):
        return a - b
    
    def multiple(a,b):
        return a * b

class math2(MathsOperation):

    def add(self,a,b):
        return a + b + b
    


print(MathsOperation.add(2,3))
print(MathsOperation.multiple(2,3))

a1 = MathsOperation()
print(a1.add(2,8))

# print(math2.add(2,3))
# print(math2.add(2,3))

print("===================")
m2 = math2()
print(m2.add(2,3))


# Getter/Setter property
# 1 - @property

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Salary can't be Negative"

        self._salary = value

emp1 = Employee("John", "5000")
print(emp1.salary)
emp1.salary = 6000

print(emp1.salary)

# Mixin
class LoggingMixin:
    def log(self, message):
        print(f"[lOG]: {message}")

class Database(LoggingMixin):
    def save(self,data):
        self.log(f"Saving {data} to database")

db = Database()
db.save("User Data")


# Magic dundon

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y +  other.y)

    def __str__(self):
        return f"Vector is ({self.x}, {self.y})"


v1 = Vector(2,3)
v2 = Vector(2,5)

# print(v1+v2)

result = v1+v2

print(result.__str__())
print("=====================")
print(str(v1+v2))



