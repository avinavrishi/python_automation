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

# def average_score_of_specific_student(grades,name):
#     for i,value in grades.items():
#         if i==name:
#             avg=sum(value)/len(value)
#     return avg

# def add_new_score_grades(grades,name,marks):
#     grades.update({name:marks})
#     return grades

# def student_highest_average_score(grades):
#     avg_list={}
#     for i,value in grades.items():
#             avg=sum(value)/len(value)
#             avg_list.update({i: avg})

#     my_values = avg_list.values()
#     for i, value in avg_list.items():
#         if value==max(my_values):
#             return i


# grades = {
#     "Alice": [85, 90, 78],
#     "Bob": [72, 88, 91],
#     "Charlie": [92, 87, 85]
# }

# name=input("Enter the students name to calculate average marks: ")
# print(f"The average marks of {name} is {average_score_of_specific_student(grades,name)}")

# name=input("Enter the students name to add : ")
# marks=list(input("Enter the list of marks ").split())
# print(f"New list is {add_new_score_grades(grades,name,marks)}")

# print(f"The name of the student with the highest average score is {student_highest_average_score(grades)}")

'''3. Employee Records
A company tracks its employees using a dictionary where the key is the employee ID and 
the value is another dictionary with their details:

employees = {
    "E001": {"name": "Alice", "department": "HR", "salary": 50000},
    "E002": {"name": "Bob", "department": "IT", "salary": 60000},
    "E003": {"name": "Charlie", "department": "Finance", "salary": 55000}
}
Write a function that:

Returns the details of an employee based on their ID.
Updates the salary of a specific employee.
Adds a new employee to the records.'''

# def employee_based_on_their_ID(employee, emp_id):
#     for i,value in employee.items():
#         if i==emp_id:
#             return value

# def salary_specific_employee(employee, emp_id, updated_salary):
#     for i,value in employee.items():
#         if i==emp_id:
#             value.update({"salary":updated_salary})
#     return employee        
            
# def new_employee_records(employees,emp_id,emp_name,emp_dept,emp_salary):
#     emp_detail={}
#     emp_detail.update({"name": emp_name, "department": emp_dept, "salary": emp_salary})
#     employees.update({emp_id:emp_detail})
#     return employees


# employees = {
#     "E001": {"name": "Alice", "department": "HR", "salary": 50000},
#     "E002": {"name": "Bob", "department": "IT", "salary": 60000},
#     "E003": {"name": "Charlie", "department": "Finance", "salary": 55000}
# }

# # emp_id=input("Enter Empoyee ID: ")
# # emp_details=employee_based_on_their_ID(employees,emp_id)
# # for key, value in emp_details.items():
# #     print(key, value)
    
# # updated_salary=int(input("Enter new salary : "))
# # print(f"Updated Empolyee list is {salary_specific_employee(employees,emp_id,updated_salary)}")   
    
# emp_id=input("Enter Employee ID")
# emp_name=input("Enter Employee Name")
# emp_dept=input("Enter Employee Department")
# emp_salary=input("Enter Employee Salary")

# print(new_employee_records(employees,emp_id,emp_name,emp_dept,emp_salary))

'''3.4. University Course Management
A university tracks courses and enrolled students using a nested dictionary, 
where the key is the course name, and the value is another dictionary with 
details like the professor's name and a list of enrolled students:

courses = {
    "Math101": {
        "professor": "Dr. Smith",
        "students": ["Alice", "Bob", "Charlie"]
    },
    "Physics101": {
        "professor": "Dr. Brown",
        "students": ["Alice", "David"]
    },
    "Chemistry101": {
        "professor": "Dr. Taylor",
        "students": ["Bob", "Charlie", "Eve"]
    }
}
Write a function that:

Returns a list of courses a specific student is enrolled in.
Adds a new student to a specific course.
Finds the course with the maximum number of students.'''

# def list_of_courses_specific_student(courses,stud_name):
#     course_list=[]
#     for i,value in courses.items():
#         if stud_name in (value["students"]):
#             course_list.append(i)
#     return course_list

# def add_student_to_specific_course(courses,stud_name,course_name):
#     new_dict_courses=courses.copy()
#     for i,value in new_dict_courses.items():
#         if i==course_name:
#            courses.update({"students":value["students"].append(stud_name)})
#     return courses
    
# def course_with_maximum_number_students(courses):
#     new_dict={}
#     for i,value in courses.items():
#         new_dict.update({len(value["students"]):value["students"]})
#         # print(value["students"])
#         # print(len(value["students"]))
#     print(new_dict)    

# # courses = {
#     "Math101": {
#         "professor": "Dr. Smith",
#         "students": ["Alice", "Bob", "Charlie"]
#     },
#     "Physics101": {
#         "professor": "Dr. Brown",
#         "students": ["Alice", "David"]
#     },
#     "Chemistry101": {
#         "professor": "Dr. Taylor",
#         "students": ["Bob", "Charlie", "Eve"]
#     }
# }

# stud_name=input("Enter Student: ")
# course_list=list_of_courses_specific_student(courses,stud_name)
# print(f"The list of courses {stud_name} is enrolled in")
# for i in course_list:
#     print(i)

# stud_name=input("Enter Student: ")
# course_name=input("Enter Course: ")
# course=add_student_to_specific_course(courses,stud_name,course_name)
# print(course)

# course_with_maximum_number_students(courses)


'''5. Library System
A library keeps track of books and their availability using a nested dictionary.
 The key is the genre, and the value is another dictionary where the key is the book title
   and the value is a dictionary of details like the author's name and the number of 
   copies available:

library = {
    "Fiction": {
        "1984": {"author": "George Orwell", "copies": 4},
        "Brave New World": {"author": "Aldous Huxley", "copies": 2}
    },
    "Science": {
        "A Brief History of Time": {"author": "Stephen Hawking", "copies": 3},
        "The Selfish Gene": {"author": "Richard Dawkins", "copies": 1}
    },
    "History": {
        "Sapiens": {"author": "Yuval Noah Harari", "copies": 5}
    }
}
Write a function that:

Returns a list of all books by a specific author.
Checks if a specific book is available (i.e., copies > 0).
Reduces the number of copies of a book after it has been borrowed.'''

# def list_of_books_specific_author(library,auth_name):
#     my_list=[]
#     for i, ivalue in library.items():
#         for j, jvalue in ivalue.items():
#             if jvalue["author"]==auth_name:
#                 my_list.append(j)
#     return my_list

# def specific_book_available(library,book_name):

#     for i, ivalue in library.items():
#         for j, jvalue in ivalue.items():
#             if j==book_name and jvalue["copies"]>0:
#                 return "book Present"
#             else:
#                 return "book Not Present"
                    
# def reduce_copy_after_borrowed(library,book_name):
#     new_library=library.copy()
#     for i, ivalue in new_library.items():
#         for j, jvalue in ivalue.items():
#             if j==book_name:
#                 print(jvalue["copies"])
#                 jvalue.update({"copies":jvalue["copies"]-1})
#     return library



# library = {
#     "Fiction": {
#         "1984": {"author": "George Orwell", "copies": 4},
#         "Brave New World": {"author": "Aldous Huxley", "copies": 2}
#     },
#     "Science": {
#         "A Brief History of Time": {"author": "Stephen Hawking", "copies": 3},
#         "The Selfish Gene": {"author": "Richard Dawkins", "copies": 1}
#     },
#     "History": {
#         "Sapiens": {"author": "Yuval Noah Harari", "copies": 5}
#     }
# }

# # auth_name=input("Enter the author name: ")
# # print(f"List of all books by a {auth_name} is : ")
# # for i in list_of_books_specific_author(library,auth_name):
# #     print(i)

# book_name=input("Enter the book name: ")
# # print(specific_book_available(library,book_name))

# reduce_copy_after_borrowed(library,book_name)


'''6. Travel Agency Booking System
A travel agency manages its bookings and customer information using a combination of 
lists, tuples, sets, and dictionaries. Here's the data structure they use:

# List of available packages (each package is a tuple containing destination and cost)
packages = [
    ("Paris", 1500),
    ("New York", 1200),
    ("Tokyo", 2000),
    ("London", 1800),
]

# Customer data stored in a dictionary
customers = {
    "C001": {
        "name": "Alice",
        "booked_packages": [("Paris", 1500), ("London", 1800)],
        "preferences": {"sightseeing", "shopping"}
    },
    "C002": {
        "name": "Bob",
        "booked_packages": [("Tokyo", 2000)],
        "preferences": {"adventure", "nature"}
    },
    "C003": {
        "name": "Charlie",
        "booked_packages": [],
        "preferences": {"shopping", "luxury"}
    }
}

# Set of popular destinations
popular_destinations = {"Paris", "New York", "Tokyo"}

Task
Write a function (or multiple functions) to handle the following tasks:

1. List Popular Packages
Return a list of all packages where the destination is in the popular_destinations set.

2. Add a Booking
Write a function that:
- Takes a customer ID, a destination, and the cost of the package as input.
- Adds the package to the customer's booked_packages list in the dictionary.
- If the customer does not exist, raise a ValueError.

3. Find Customers by Preference
Write a function that takes a preference (e.g., "shopping") as input and returns a set of customer names who have that preference.

4. Calculate Total Revenue
Write a function that calculates and returns the total revenue generated from all booked packages.

5. Find Frequent Travelers
Write a function that:
- Returns the name of the customer who has booked the most packages.
- If there's a tie, return all names in a set.'''
