import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Art2@asDjk&$56",
    database="pythondb"
)

mycursor=mydb.cursor()
while True:
    userinput=input("""
1 Type 'add' for adding new task
2 Type 'complete' for completing the task
3 Type 'show' for showing all the task 
4 Type 'completeAll' for completing all the task
5 Type 'edit' for editing a task                                      
6 Type 'exit' for exiting the from the application                                             
""")
    match userinput:
        case "add":
            task=input("Enter the task that you want to add in todo: ")
            query="INSERT INTO Todo (Task) VALUES (%s)"
            mycursor.execute(query,[task])
            mydb.commit
            print("Task added")
        case "show":
            select_query = "SELECT * FROM Todo;"
            mycursor.execute(select_query)

            # Fetch all rows
            results = mycursor.fetchall()

            # Display the data
            print("ID | Task")
            print("---|--------------------------------")
            for row in results:
                print(f"{row[0]}  | {row[1]}")
        case "complete":
            id=int(input("Enter the ID of the task to complete: "))
            delete_query = "DELETE FROM Todo WHERE id = %s"
            task_id = (id,)  # Replace with the ID of the row you want to delete

            # Execute the deletion
            mycursor.execute(delete_query, task_id)
            mydb.commit() 
        case "edit":
            id=int(input("Enter id of the task to edit: "))   
            update_query = "UPDATE Todo SET Task = %s WHERE id = %s"
            new_task = input("Enter the task")  # New task description
            mycursor.execute(update_query, (new_task,id))
            mydb.commit() 
        case "completeAll":
            delete_query="DELETE FROM Todo"
            mycursor.execute(delete_query)
            mydb.commit() 
        case "exit":
            break    
        case _:
            print("Invalid Input!")  

mydb.close()



    