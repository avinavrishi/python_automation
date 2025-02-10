import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

print(type(mycursor))

for x in mycursor:
    print(x)

print("====================")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="studentdb"
)

mycursor = mydb.cursor()

mycursor.execute("Show tables")

tables = []
for x in mycursor:
    print(x)
    tables.append(x[0])

print("====================")


mycursor.execute("select * from students")
for x in mycursor:
    print(x)

print("========================")

if "faculty" not in tables:
    sql_query = "CREATE TABLE faculty (faculty_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20) NOT NULL, email VARCHAR(20), department VARCHAR(20))"
    mycursor.execute(sql_query)

    insert_query = "INSERT INTO faculty(name, email, department) VALUES (%s, %s, %s)"
    value = ("Manish", "manish@gmail.com", "Science")
    mycursor.execute(insert_query, value)
    mydb.commit() # To make the actual changes in the database.
    print(mycursor.rowcount, "record inserted") # This give result only on insert

else:

    # To insert multiple items in db
    # insert_query = "INSERT INTO faculty(name, email, department) VALUES (%s, %s, %s)"
    # value = [("Suraj", "suraj@gmail.com", "Science"), ("Amit", "amit@gmail.com", "Commerce")]
    # mycursor.executemany(insert_query, value)
    # mydb.commit() # To make the actual changes in the database.

    # print(mycursor.lastrowid, "record inserted")

    mycursor = mydb.cursor()

    mycursor.execute("select * from faculty")
    myresult = mycursor.fetchall()
    print(type(myresult))

    for x in myresult:
        print(x)

    print("====================")

    mycursor.execute("select * from faculty")
    myresult = mycursor.fetchone()
    print(myresult)

    print("=======================")


    mycursor = mydb.cursor()
    mycursor.execute("select * from students")
    students_result = mycursor.fetchall()  # Fetch all student data
    for student in students_result:
        print(student)

