'''Create a base class LibraryMember with:

Attributes: member_id, name, and borrowed_books (a list of book names).
Methods:
borrow_book(book_name): Adds the book to the borrowed_books list.
return_book(book_name): Removes the book from the list.
Create a derived class StudentMember that inherits from LibraryMember:

Additional Attribute: max_books (default is 3).
Override borrow_book to check if the student has reached the maximum borrow limit.
If so, do not allow borrowing.

Tasks:
Create a student object, borrow three books, and try borrowing one more.
Return a book and borrow again.'''

# class LibraryMember:
#     max_book=3

#     def __init__(self,member_id,name,borrowed_books):
#         self.member_id=member_id
#         self.name=name
#         self.borrowed_books=borrowed_books

#     def borrow_book(self):
#         if self.max_book<=len(self.borrowed_books):
#             print(f"{self.name} has reached the maximum borrow limit")
#         else:
#             print(f"{self.name} can borrow {self.max_book-len(self.borrowed_books)} more books")

# class Studentmember(LibraryMember):
#     def borrow_book(self,book_name):
#         if self.max_book<=len(self.borrowed_books):
#             print(f"{self.name} has reached the maximum borrow limit")
#             print(self.borrowed_books)
#         else:
#             self.borrowed_books.append(book_name)
#             print(f"{self.name} borrowed {book_name}")
#             print(self.borrowed_books)

#     def return_book(self,book_name):
#         self.borrowed_books.remove(book_name)
#         print(f"{self.name} returned {book_name}")
#         print(self.borrowed_books)
        
# s1=Studentmember("S001","Max",["ABC","XYZ","LMN"])
# s1.borrow_book("EFG")
# s1.return_book("XYZ")
# s1.borrow_book("EFG")
# # s2=Studentmember("S002","Alex",["Epic","Steam","RIT"])
# # s2.borrow_book("RIHigh")
# # s2.return_book("RIT")

# # s3=LibraryMember("S001","Max",["ABC","XYZ","ABC","XYZ"])
# # s3.borrow_book()

'''Create a system to manage e-commerce sellers.
Define:
Seller class:
Attributes: seller_id, name, and products (a dictionary with product name as the key and price
as the value).
Method: add_product(product_name, price).

Account class:
Attributes: account_balance.
Method: withdraw(amount) to reduce balance.

EcommerceSeller class (inherits both Seller and Account):
Method: sell_product(product_name) to remove the product from products and add its price 
to the account_balance.

Tasks:
Create a seller with products and account balance.
Sell a product and verify that it is removed from the inventory and the balance is updated.
Try withdrawing money and handle cases where the balance is insufficient.'''

# class Seller:
#     def __init__(self,seller_id, name, products):
#         self.seller_id=seller_id
#         self.name=name
#         self.products=products

#         print(products)

    
#     def add_product(self,product_name,price):
#         self.products.update({product_name:price})
#         print(self.products)
#         return sum(self.products.values())

# class Account:
#     def __init__(self,account_balance):
#         self.account_balance=account_balance

#     def withdraw(amount):
#         pass

# class EcommerceSeller(Seller,Account):
#     def __init__(self, seller_id, name, products):
#         super().__init__(seller_id, name, products)
#         Account.__init__(self,self.account_balance)

        
#     def sell_product(self,product_name):
#         del self.products[product_name]
#         print(self.products)

# s1=Seller("S001","Max",{"Bottle":40,"Pen":25})
# acc_balance=s1.add_product("Cup",20)
# print(acc_balance)

# a1=Account(acc_balance)

# e1=EcommerceSeller()
# e1.sell_product("Pen")

'''Create a base class Vehicle:

Attributes: vehicle_id, make, and maintenance_records (a list of tuples containing date 
and service performed).
Method: add_maintenance(date, service) to append a record.
Create derived classes Car and Truck:

Additional Attributes:
Car: fuel_type (e.g., petrol or diesel).
Truck: cargo_capacity (in tons).

Add unique methods:
Car: check_fuel() - Returns the fuel type.

Truck: check_cargo_limit(limit) - Compares the limit with the cargo capacity.

Tasks:
Add maintenance records for a car and truck.
Call their unique methods and display the details.'''

# class Vehicle:
    
#     def __init__(self,vehicle_id,make,maintenance_record):
#         self.vehicle_id=vehicle_id
#         self.make=make
#         self.maintenance_record=maintenance_record
    
#     def add_maintenance(self,date,service):
#         self.my_tuple=(date,service)
#         self.maintenance_record.append(self.my_tuple)
#         print(self.maintenance_record)

# class Car(Vehicle):
#     check_fuel_type="Petrol"
#     def check_fuel(self):
#         return self.check_fuel_type

# class Truck(Vehicle):
#     check_capacity=200
#     def check_cargo_limit(self,limit):
#         if self.check_capacity>limit:
#             print("Cargo capacity is in the limit")
#         else:
#             print("Cargo capacity is more than limit")    

# c1=Car("C001","Honda",[("1/1/2023","Servicing"),("10/4/2024","Oiling")])
# c1.add_maintenance("4/6/2024","Wheel Alignment")
# fuel_type=str(c1.check_fuel())
# print(f"Vehicles fuel type is :{fuel_type}")


'''Design a system for smart home devices using hybrid inheritance.
Define:

Device class (base class):
Attributes: device_id, status (on/off).
Method: toggle() to switch the status.

Appliance class (inherits Device):
Additional Attribute: power_rating (watts).
Method: calculate_energy(hours) to return energy consumption.

Sensor class (inherits Device):
Additional Attribute: sensitivity_level.
Method: adjust_sensitivity(level) to change the level.

SmartHomeDevice class (inherits both Appliance and Sensor):
Additional Method: device_summary() to print all attributes.

Tasks:
Create a smart home device with both appliance and sensor features.
Toggle the device status, adjust the sensitivity, and calculate energy usage.'''


class Device:
    def __init__(self,device_id,status):
        self.device_id=device_id
        self.status=status

    def toggle(self):
        if self.status=="ON":
            self.status="OFF"
            print(self.status)
        else:
            self.status="ON"    
            print(self.status)

class Appliance(Device):
    def __init__(self, device_id, status,power_rating):
        super().__init__(device_id, status)
        self.power_rating=power_rating

    def calculate_energy(self,hours):
        return hours*self.power_rating

class Sensor(Device):
    def __init__(self, device_id, status,sensitivity_level):
        super().__init__(device_id, status)
        self.sensitivity_level=sensitivity_level
   
    def adjust_sensitivity(self,level):
        pass

class SmartHomeDevice(Appliance,Sensor):
    def device_summary():
        pass

# d1=Device("D001","ON")

a1=Appliance("D001","ON",200)
a1.toggle()
energy_comsumption=a1.calculate_energy(2)
print(f"Energy comsumed by device is {energy_comsumption} watts")
