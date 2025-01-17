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

class University():
#     max_courses_per_student={"Science":20,"Commerce":25,"Art":30,"Dairy Science":15,"ITI":40}
    max_courses_per_student=[] 
    total_students_enrolled=[]
    
    def __init__(self,student_name,student_id,enrolled_courses):
        self.student_name
        self.student_id
        self.enrolled_courses=[] 
    
    def enroll_student_course(self,student_name,enrolled_courses):
        
        




# u1=University(student_name,student_id,enrolled_courses)


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

class ShoppingCart():
    discount_rate=0

    def __init__(self,cart_id,items,total):
        self.cart_id=cart_id
        self.items=items
        self.total=total
    
    def add_item(self,):

s1=ShoppingCart(10,{"Body Soap":(20,5), "Shampoo":(150,2),"Toothpaste":(45,2)},490)