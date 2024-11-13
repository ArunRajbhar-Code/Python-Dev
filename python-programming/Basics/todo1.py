todos=[]
while True:
    user_Action=input("""
1 Type 'add' for adding to dos
2 Type 'show' for showing all the to dos
3 Type 'exit' for close the program 
4 Type 'edit' for editing the to do    
5 Type 'complete' for completing the to do                                                                                  
""")
    match user_Action.strip():# strip function is used to remove spaces 
        case "add":
            todo=input("Enter the todo ")
            todos.append(todo.capitalize())
        case "show":
            print("List of task to do".upper())
            for index,i in enumerate(todos):
                print(index+1,"-",i)
        case "edit":
            print("List of task to do".upper())
            for index,i in enumerate(todos):
                print(index+1,"-",i)
            number=int(input("Please enter the no of to do to edit :"))
            todo=input(f"current value of to do is '{todos[number-1]}' Please enter new to do :")
            todos[number-1]=todo
        case "complete":
            number=int(input("Please enter the no of to do to complete :"))
            todos.pop(number-1)
        case "exit":
            break    
        case _:
            print("Invalid Input!")    
    