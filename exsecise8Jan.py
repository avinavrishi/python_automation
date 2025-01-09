'''1. A teacher keeps track of student attendance using a list of tuples:
attendance = [("Alice", "Present"), ("Bob", "Absent"), ("Charlie", "Present")]
Write a function to count how many students are "Present" in the class.'''

def present_student(attendance_list):
    count=0
    for i in range(0, len(attendance_list)):
        if ((attendance_list[i])[1])=="Present":
            count+=count
    return(count)

print()

attendance = [("Alice", "Present"), ("Bob", "Absent"), ("Charlie", "Present")]
present_count=int(present_student(attendance))
print(f"Total present students are {present_count}")
print()

''' A company needs to validate email addresses. Write a function that checks if an email is valid.
Rules for validity : The email must contain "@" and ".".
Return "Valid Email" if both conditions are met. Otherwise, return "Invalid Email".
'''

# def email(email):
#     if email=="":
#         print("please Enter valid Email ID")
#     elif "@" in email and "." in email:
#          print("Valid Email ID")
#     else:
#         print("Invalid Email ID")
    
# print()
# userEmail=input("Enter valid Email ID : ")
# email(userEmail)
# print()

'''A grocery store stores its inventory as a list of tuples:
inventory = [("Apples", 50), ("Bananas", 20), ("Oranges", 0)]
Write a function to check if an item is in stock.
The function should return:
"In Stock" if the quantity is greater than 0.
"Out of Stock" otherwise.
# '''
# def checkitem(item_to_check):
#     is_in_stock=False
#     for i in range(len(inventory)):   
#        if item_to_check in inventory[i]:
#         is_in_stock=True
#         item=inventory[i]
#         if item[1]>0:
#            print("Item is in stock")
#         else:
#            print("Item is out of stock")      

#     if is_in_stock==False:
#        print("Please enter valid item")          
# print()
# inventory=[("Apples", 50), ("Bananas", 20), ("Oranges", 0)]
# item=input("Enter the item you want to buy : \n")
# checkitem(item)
# print()

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