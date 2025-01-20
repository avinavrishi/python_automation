# Topic Access Specifier
# All attributes and method are by default public
class Example:
    def __init__(self):
        self.public_attr = "I am public"

    def public_method(self):
        print("Public Method")

obj1 = Example()
print(obj1.public_attr)

print("============================")

# Protected Access Specifier
# Syntax - (Single Underscore _)

class Example2:
    def __init__(self):
        self._protected_attr = "I am protected"
        print("Constructor")

    def _protected_method(self):
        print("Protected Method")

class Example_child(Example2):    
    def method_2(self):
        self._protected_method()
        print("Child Method")


obj3 = Example_child()
obj3.method_2()

obj3._protected_method() # This also work, but it is not recommend


print("=========================")


# Private access specifier
# Syntax - Double underscore __

class Example3:
    def __init__(self):
        self.__private_attr = "I am private"
        print("Constructor Example 3")

    def __private_method(self):
        print("Private Method")

    def parent_method(self):
        self.__private_method()

class Example3_child(Example3):    
    def method_3(self):
        print("Child Method")
        self.parent_method()


obj4 = Example3_child()
obj4.method_3()
print("=================")

obj5 = Example3()
obj5.parent_method()