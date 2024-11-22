import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Art2@asDjk&$56",
    database="pythondb"
)

mycursor=mydb.cursor()

# mycursor.execute("""CREATE TABLE Todo (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         Task VARCHAR(255) NOT NULL
#     );""")

# insert_query = "INSERT INTO Todo (Task) VALUES (%s)"
# tasks = [
#         ("Finish Python project",),
#         ("Study MySQL syntax",),
#         ("Buy groceries",),
#         ("Exercise for 30 minutes",)
#     ]
# mycursor.executemany(insert_query, tasks)
# mydb.commit()  # Commit the transaction

# print(f"{mycursor.rowcount} records inserted successfully into 'Todo' table.")



    # SQL query to select all data from the Todo table
select_query = "SELECT * FROM Todo;"
mycursor.execute(select_query)

    # Fetch all rows
results = mycursor.fetchall()

    # Display the data
print("ID | Task")
print("---|--------------------------------")
for row in results:
        print(f"{row[0]}  | {row[1]}")