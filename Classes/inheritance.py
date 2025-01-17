# Topic Inheritance

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def printname(self):
        print(self.first_name, self.last_name)


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)




s1 = Student("Alice", "Cooper")
s1.printname()
