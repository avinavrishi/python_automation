'''1. A teacher keeps track of student attendance using a list of tuples:
attendance = [("Alice", "Present"), ("Bob", "Absent"), ("Charlie", "Present")]
Write a function to count how many students are "Present" in the class.'''

# def present_student(attendance_list):
#     count=0
#     for i in range(0, len(attendance_list)):
#         if ((attendance_list[i])[1])=="Present":
#             count+=1
    
    
#     # Upgrade algorithm 2
#     for i in attendance_list:
#         if i[1] == "Present":
#             count+=1

#     # Upgrade algorithm 2
#     data = sum([1 for i in attendance_list if i[1] == "Present"])

#     return(count)


# attendance = [("Alice", "Present"), ("Bob", "Absent"), ("Charlie", "Present")]
# present_count=int(present_student(attendance))
# print(f"Total present students are {present_count}")
# print()

#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------

''' A company needs to validate email addresses. Write a function that checks if an email is valid.
Rules for validity : The email must contain "@" and ".".
Return "Valid Email" if both conditions are met. Otherwise, return "Invalid Email".
'''

# def email(email):
#     if len(email)==0 or " " in email:
#         return "Invalid Email ID"

#     if email.count("@") == 1:
#         if "@" in email and "." in email:
#             return "Valid Email ID"
#         else:
#             return "Invalid Email ID"

#     # Upgrade Algorithm 2
#     validate_email = "Valid Email" if '@' in email and '.' in email else "Invalid Email" if len(email)==0 or " " in email else "Invalid Email"
    
#     return "Invalid Email ID"


    
# print()
# userEmail=input("Enter valid Email ID : ")
# print(email(userEmail))

'''A grocery store stores its inventory as a list of tuples:
inventory = [("Apples", 50), ("Bananas", 20), ("Oranges", 0)]
Write a function to check if an item is in stock.
The function should return:
"In Stock" if the quantity is greater than 0.
"Out of Stock" otherwise.
# '''

# def checkitem(item_to_check, inventory):
#     for i in range(len(inventory)):   
#        if item_to_check in inventory[i]:
#         item=inventory[i]
#         if item[1]>0:
#            return "Item is in stock"
#         else:
#            return "Item is out of stock"      

#     return "Please enter valid item"          

# print(checkitem(input("Enter the item you want to buy : \n"), [("Apples", 50), ("Bananas", 20), ("Oranges", 0)]))


'''An e-commerce system stores items in a cart as a list of tuples:
cart = [("Laptop", 1, 800), ("Mouse", 2, 20), ("Keyboard", 1, 50)]
Each tuple contains the item name, quantity, and price per item.
Write a function calculate_total(cart) that calculates the total cost of all items in the cart. 
Apply a 10% discount if the total cost exceeds $500.'''


# def calculate_total(cart_input):
#     cost=0
#     for i in range (0,len(cart)):
#         cost+=(((cart_input[i])[1])*((cart_input[i])[2]))
#     return(cost)    

# cart = [("Laptop", 1, 800), ("Mouse", 2, 20), ("Keyboard", 1, 50)]
# total_cost=calculate_total(cart) 
# print()
# print(f"Total Cost of the cart is : {total_cost}")
# if total_cost>=500:
#     discount=(total_cost*10)/100
#     print(f"Total Cost to pay after discount : {total_cost-discount}")
# print()

'''5. A flight management system stores flight details as tuples:
flights = [("AI101", "New York", "London", "10:00 AM"), ("AI102", "London", "Paris", "12:00 PM"), ("AI103", "New York", "Toronto", "02:00 PM")]

Write a function find_flights(city, flights) that returns a list of all flights originating
from a given city. If no flights are found, return "No flights available."'''

# def find_flights(city, flights):
#     flight_list=[]
    
#     for i in range(0,len(flights)):
#         # print((flights[i])[1])
#         if (flights[i])[1]==city:
#             flight_list.append(flights[i])
#     return(flight_list)

# print()
# flights = [("AI101", "New York", "London", "10:00 AM"), ("AI102", "London", "Paris", "12:00 PM"), ("AI103", "New York", "Toronto", "02:00 PM")]
# orig_city=input("Please enter city of origin : \n")
# print()
# list_of_flights=[find_flights(orig_city,flights)]
# print(f"The list of all flights originating from {orig_city} is ")
# print(list_of_flights)
# print()

'''6. A library keeps track of books in a list of tuples:
books = [("Book A", "Available"), ("Book B", "Borrowed"), ("Book C", "Available")]

Write a program with the following functionalities:
A function list_books(status) that lists all books with a given status 
(e.g., "Available" or "Borrowed").

A function borrow_book(book_name) that changes the status of a book to "Borrowed" 
if it is "Available". If the book is already borrowed, return "Book is already borrowed."

A function return_book(book_name) that changes the status of a book to "Available". 
If the book is not borrowed, return "Book is already available."'''

# def list_books(status):
#      book_list=[]
#      for i in range(0,len(books)):
#           if (books[i])[1]==status:
#               book_list.append(books[i])
#      return(book_list) 
    
# def borrow_book(book_name):
#      new_list=[]
#      for i in range(0,len(books)):
#           if(books[i])[0]==book_name:
#            if (books[i])[1]=="Available":
#                new_list=list(books[i])
#                new_list[1]="Borrowed"
#                books[i]=new_list
#                print(books)
#            else:
#                print("Book is already borrowed.")               
            
# def return_book(book_name):
#      new_list=[]
#      for i in range(0,len(books)):
#           if(books[i])[0]==book_name:
#            if (books[i])[1]=="Borrowed":
#                new_list=list(books[i])
#                new_list[1]="Available"
#                books[i]=new_list
#                print(books)
#            else:
#                print("Book is available.")               

# print()
# books = [("Book A", "Available"), ("Book B", "Borrowed"), ("Book C", "Available")]
# status_of_book=input("Available or Borrowed : \n")
# available_books_list=[list_books(status_of_book)]
# print(f"List of {status_of_book} books is {available_books_list}")
# print()
# print("#########################################################")
# print()
# book1=input("Enter the book name you want to borrow : \n")
# borrow_book(book1)
# print()
# print("#########################################################")
# print()
# book2=input("Enter the book name to return: \n")
# return_book(book2)
# print()

'''7. An event organizer tracks registrations as a list of tuples:
registrations = [("Alice", "Paid"), ("Bob", "Not Paid"), ("Charlie", "Paid")]

Write a program with the following functionalities:

A function get_paid_registrations() that returns a list of all participants who have paid.

A function mark_paid(name) that updates the status of a participant to "Paid". 
If the participant does not exist, return "Participant not found."

A function count_status() that returns a dictionary with the count of "Paid" 
and "Not Paid" participants.'''

def get_paid_registrations(parti_list):
    for i in range(0, len(parti_list)):
        if (parti_list[i])[1]=="Paid":
            paid_list.append((parti_list[i])[0])        
    return (paid_list)


def mark_paid(name):
    is_paid=False
    is_available=True
    
    for i in range(0,len(registrations)):
        if (registrations[i])[0]==name and (registrations[i][1]=="Not Paid"):
            is_paid=True
            my_list=list(registrations[i])
            my_list[1]="Paid"
            registrations[i]=my_list
            print(registrations)
        elif (registrations[i])[0]!=name:
            is_available=False
    if is_paid==False:   
        print("Already Paid")

def count_status(registration):
    paid_count=0
    unpaid_count=0
    for i in registration:
        if i[1]=="Paid":
            paid_count+=1
        elif i[1]=="Not Paid":
            unpaid_count+=1    
    return paid_count,unpaid_count
    

registrations = [("Alice", "Paid"), ("Bob", "Not Paid"), ("Charlie", "Paid")]
paid_list=[]
paid_list=get_paid_registrations(registrations)
print(f"The list of all paid participants is {paid_list}")
print()
print("#########################################################")
print()
paid_name=input("Enter the name who paid the fees : ")
mark_paid(paid_name)
paid_c,unpaid_c=count_status(registrations)
print(f"Paid Count is : {paid_c}")
print(f"Unpaid Count is : {unpaid_c}")
print()