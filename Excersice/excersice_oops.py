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
#             self.update_year=year
#             return self.update_year
#         else:
#             return "Book is not available" 

#     def final_details(self):
#         print(f"The name of the book is {self.title} written by{self.author} published in {self.update_year} and available copies of the book are {self.copies_available}")

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

class Product():
    def __init__(self,product_name, price,quantity):
        self.product_name=product_name
        self.price=price
        self.quantity=quantity

    def restock(self,quantity):
        self.quantity=self.quantity+quantity
    
    def sell(self,quantity):
        self.quantity=self.quantity-quantity

    def change_price(self,New_price):
        self.price=New_price

    def final_details(self):
        print(f"The name of the product is {self.product_name} of price {self.price} and the total pieces are {self.quantity}")    

p1=Product("Laptop",1000,10)
p1.restock(5)
p1.sell(7)
p1.change_price(1200)
p1.final_details()
