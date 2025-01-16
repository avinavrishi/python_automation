'''1.1. Bookstore Inventory
A bookstore keeps track of its inventory using a dictionary, where the keys are book titles 
and the values are the number of copies available:

inventory = {
    "The Great Gatsby": 10,
    "1984": 5,
    "To Kill a Mockingbird": 8
}
Write a function that:

Updates the stock of a book after a sale (reduce the count).
Adds a new book to the inventory with its stock.
Returns the title of the book with the highest stock.'''

# def stock_after_sale(inventory,book,count):
#     for data in inventory:
#         if data==book:
#             inventory.update({book:inventory[book]-count})
#     return inventory

# def add_new_book(inventory,book,count):
#     inventory.update({book:count})
#     return inventory

# def book_with_the_highest_stock(inventory):
#     my_values = inventory.values()
#     # return max(my_values)
#     for i, value in inventory.items():
#         if value==max(my_values):
#             return i

# inventory = {
#     "The Great Gatsby": 10,
#     "1984": 5,
#     "To Kill a Mockingbird": 8
# }
# book=input("Which book do you want to purchase : \n")
# count=int(input("How many books do you want to purchase : \n"))
# res=stock_after_sale(inventory,book,count)
# print(res)

# book=input("Which book do you want to add : \n")
# count=int(input("How many books do you want to add : \n"))
# res=add_new_book(inventory,book,count)
# print(res)

# print(f"The book with the highest stock is \n{book_with_the_highest_stock(inventory)}")

'''2. Student Grades Management
A teacher stores students' grades for a subject in a dictionary, 
where the key is the student's name and the value is a list of their scores:

grades = {
    "Alice": [85, 90, 78],
    "Bob": [72, 88, 91],
    "Charlie": [92, 87, 85]
}
Write a function that:

Calculates the average score of a specific student.
Adds a new score to a student's list of grades.
Returns the name of the student with the highest average score.'''

def average_score_of_specific_student(grades,name):
    for i,value in grades.items():
        if i==name:
            avg=sum(value)/len(value)
    return avg

def add_new_score_grades(grades,name,marks):
    grades.update({name:marks})
    return grades

def student_highest_average_score(grades):
    avg_list={}
    for i,value in grades.items():
            avg=sum(value)/len(value)
            avg_list.update({i: avg})

    my_values = avg_list.values()
    for i, value in avg_list.items():
        if value==max(my_values):
            return i


grades = {
    "Alice": [85, 90, 78],
    "Bob": [72, 88, 91],
    "Charlie": [92, 87, 85]
}

# name=input("Enter the students name to calculate average marks: ")
# print(f"The average marks of {name} is {average_score_of_specific_student(grades,name)}")

# name=input("Enter the students name to add : ")
# marks=list(input("Enter the list of marks ").split())
# print(f"New list is {add_new_score_grades(grades,name,marks)}")

print(f"The name of the student with the highest average score is {student_highest_average_score(grades)}")