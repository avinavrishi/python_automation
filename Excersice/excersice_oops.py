'''1. Library Book Tracker
Create a Book class to track books in a library. Each book object should have:

Attributes: title, author, year, and copies_available.
Methods:
borrow_book() – Decrease copies_available by 1 if there are copies available.
return_book() – Increase copies_available by 1.
update_year(new_year) – Update the year of the book.
Task:

Create a book object for "1984" by George Orwell, published in 1949 with 5 copies.
Borrow the book twice.
Update the publication year to 1950.
Print the final details of the book.'''

# class Book:

#     def __init__(self,title, author, year,copies_available):
#         self.title=title
#         self.author=author
#         self.year=year
#         self.copies_available=copies_available
    
#     def borrow_book(self,tittle):
#         if self.copies_available>0:
#             self.copies_available=self.copies_available-1
#             return self.copies_available
#         else:
#             return "Book is not available"    

#     def return_book(self,tittle):
#           if self.copies_available>0:
#             self.copies_available=self.copies_available+1
#             return self.copies_available
#           else:
#             return "Book is not available"  

#     def update_year(self,year):   
#         if self.copies_available>0:
#             self.year=year
#             return self.year
#         else:
#             return "Book is not available" 

#     def final_details(self):
#         print(f"The name of the book is {self.title} written by{self.author} published in {self.year} and available copies of the book are {self.copies_available}")

# b1=Book("1984","George Orwell",1949,5)
# copies_availabe=b1.borrow_book("1984")
# copies_availabe=b1.borrow_book("1984")
# updated_year=b1.update_year(1950)
# print()
# b1.final_details()

'''2. Customer Loyalty Program
Create a Customer class to manage a store's loyalty program. Each customer object should have:

Attributes: name, email, and points.
Methods:
add_points(points) – Add loyalty points to the customer.
redeem_points(points) – Redeem points if the customer has enough balance, 
otherwise display a message.
update_email(new_email) – Update the customer's email address.
Task:

Create a customer object for "Alice" with an initial email and 50 points.
Add 30 points to Alice's account.
Redeem 60 points.
Update Alice's email to a new one.
Print Alice's final details.'''

# class Customer():
#     def __init__(self,name,email,points):
#          self.name=name
#          self.email=email
#          self.points=points

#     def add_points(self,point):
#          self.points=self.points+point
    
#     def redeem_points(self,point):
#          self.points=self.points-point
         
#     def update_email(self,new_email):
#          self.email=new_email

#     def final_details(self):
#         print(f"The name of the customer is {self.name} his email id is {self.email} his loyalty points are {self.points}")


# c1=Customer("Alice","alice@gmail.com",50)     
# c1.add_points(30)        
# c1.redeem_points(60)
# c1.update_email("alice@yahoo.com")
# c1.final_details()
        
'''3. Product Inventory Manager
Create a Product class to manage inventory in a store. Each product object should have:

Attributes: product_name, price, and quantity.
Methods:
restock(quantity) – Add more items to the inventory.
sell(quantity) – Reduce the quantity of items if the stock is sufficient.
change_price(new_price) – Update the price of the product.
Task:

Create a product object for "Laptop" with a price of 1000 and 10 units in stock.
Restock 5 more units.
Sell 7 units.
Change the price to 1200.
Print the final details of the product.'''

# class Product():
#     def __init__(self,product_name, price,quantity):
#         self.product_name=product_name
#         self.price=price
#         self.quantity=quantity

#     def restock(self,quantity):
#         self.quantity=self.quantity+quantity
    
#     def sell(self,quantity):
#         self.quantity=self.quantity-quantity

#     def change_price(self,New_price):
#         self.price=New_price

#     def final_details(self):
#         print(f"The name of the product is {self.product_name} of price {self.price} and the total pieces are {self.quantity}")    

# p1=Product("Laptop",1000,10)
# p1.restock(5)
# p1.sell(7)
# p1.change_price(1200)
# p1.final_details()

'''University Enrollment System
Create a class University with:

Class variables: max_courses_per_student (default 5) and total_students_enrolled.
Instance attributes: student_name, student_id, and enrolled_courses (a list of course names).
Tasks:

Write a method to enroll a student in a course. If the maximum course limit is reached,   
display an error.
Add a method to drop a course by its name.
Implement a class method to change the max_courses_per_student limit.
Create a method to generate a report of all students and their enrolled courses 
(use a class-level dictionary to store student data).
Add a method to calculate the average number of courses enrolled per student.
Constraints:

Ensure total_students_enrolled is updated whenever a new student is created.
Prevent duplicate course enrollments for the same student.'''

# class University():
#     max_courses_per_student=["Science","Commerce","Art","Dairy Science","ITI"]
#     total_students_enrolled=0
#     all_students=[]
    
#     def __init__(self,student_id):
#         # self.student_name
#         self.student_id=student_id
#         self.students={}
#         self.enrolled_courses=[] 
#         University.all_students.append(self)
    
#     def enroll_student(self,student_name,enrolled_courses):

#         if len(self.students.values())>len(self.max_courses_per_student):
#             print("Exceed the cources limit")
#         else:    
#           self.students[student_name]=(enrolled_courses)
#           print("New student is added!!!")
#         #   print(self.students.values())
#         #   print(len(self.students.values()))

#     def drop_course_by_its_name(self,course_name):
#         for i in self.max_courses_per_student:
#             if i==course_name:
#                 self.max_courses_per_student.remove(i)
#         print(self.max_courses_per_student)        

#     def report_of_all_student(self):
#         summary = []
#         for i in self.all_students:
#             summary.append({
#                 'student_id': i.student_id,
#                 'Student': i.students,
#             })
#         print(f"Total Students are : {len(summary)}")
#         return summary

#     @classmethod
#     def change_max_courses_per_student_limit(self,ans,course_name):
#         if ans=="Add":
#             self.max_courses_per_student.append(course_name)
#         else:
#             self.max_courses_per_student.remove(course_name)
#         print(self.max_courses_per_student)

    
            

# u1=University("001")
# u1.enroll_student("Max",("Math","Physics","Chemistry"))
# # u1.drop_course_by_its_name("ITI")

# u2=University("002")
# u2.enroll_student("Ron",("Math","ITI","Commerce"))

# u3=University("003")
# u3.enroll_student("Alia",("Physics","ITI","Art"))

# # ans=input("Do you want to add or remove course : ")
# # new_course=input("Which course do you want to add/remove : ")
# # University.change_max_courses_per_student_limit(ans,new_course)

# report=u1.report_of_all_student()
# print(report)
 





'''Online Shopping Cart System
Create a class ShoppingCart that simulates a shopping cart system for an e-commerce platform. 
The class has:

A class variable discount_rate representing a global discount applied to all carts (default 0%).

Instance attributes for cart_id (unique), items (dictionary with item name as the key and a 
tuple of price and quantity as the value), and total.

Tasks:

Create a method to add an item to the cart. If the item already exists, update its quantity.

Implement a method to remove an item by name. If the item doesn't exist, handle gracefully.

Write a method to calculate the total price after applying the class-level discount_rate.

Add a method to update the global discount_rate for all carts.

Create a class method to generate a summary of all carts (use a class variable all_carts to
track all created carts).

Constraints:

Ensure discount_rate applies uniformly to all carts.
Handle edge cases like removing an item not in the cart or setting a negative discount rate.'''

# class ShoppingCart():
#     discount_rate=0 # Global variable 
#     all_carts = [] # Global list

#     def __init__(self,cart_id):
#         self.cart_id=cart_id
#         self.items={}
#         self.total=0
#         ShoppingCart.all_carts.append(self)
    
#     def add_item(self,item_name, price, quantity):
#         if item_name in self.items:
#             current_price , current_quantity = self.items[item_name]
#             self.items[item_name] = (price, current_quantity+quantity)
#         else:
#             self.items[item_name] = (price, quantity)
        
#         print(f"Item {item_name} has been added.")

#     def remove_item(self, item_name):
#         if item_name in self.items:
#             del self.items[item_name]
#             print("Item has been deleted.")
#         else:
#             print("Item not found.")

#     def calculate_total_price(self):
#         self.total = sum(price * quantity for price, quantity in self.items.values())
#         discounted_total = self.total * (1 - ShoppingCart.discount_rate/100)
#         return round(discounted_total, 2)

#     @classmethod # decorator
#     def update_discount_rate(cls, new_rate):
#         if new_rate < 0:
#             print("New rate can not be negative")
#         else:
#             cls.discount_rate= new_rate
#             print("Global rate updated")

#     @classmethod
#     def generate_summary(cls):
#         summary = []

#         for cart in cls.all_carts:
#             cart_total = cart.calculate_total_price()
#             summary.append({
#                 'cart_id': cart.cart_id,
#                 'total': cart_total,
#                 'items': cart.items
#             })

#         return summary


# cart1 = ShoppingCart("Cart001")
# cart2 = ShoppingCart("Cart002")

# cart1.add_item("Body Soap", 20, 5)

# cart1.add_item("Shampoo", 150, 2)

# cart2.add_item("Toothpaste", 45, 2)

# ShoppingCart.update_discount_rate(10)

# print(cart1.calculate_total_price())
# print(cart2.calculate_total_price())

# summary = ShoppingCart.generate_summary()
# print(summary)

# ShoppingCart.update_discount_rate(-5)

# # s1=ShoppingCart(10,{"Body Soap":(20,5), "Shampoo":(150,2),"Toothpaste":(45,2)},490)