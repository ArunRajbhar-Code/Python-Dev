
while True:
    user_Action=input("""
1 Type 'add' for adding to dos
2 Type 'show' for showing all the to dos
3 Type 'exit' for close the program 
4 Type 'edit' for editing the to do    
5 Type 'complete' for completing the to do  
6 Type 'completeAll' for completing all to do                                                                                                      
""")
    match user_Action.strip():# strip function is used to remove spaces 
        case "add":
            todo=input("Enter the todo ")+"\n"
            with open("todo.txt","a") as file:
                file.write(todo)
        case "show":
            print("List of task to do".upper())
            with open("todo.txt","r") as file:
                todos=file.readlines()
            for index,i in enumerate(todos):
                print(index+1,"-",i.removesuffix("\n"))
        case "edit":
            print("List of task to do".upper())
            with open("todo.txt","r") as file:
                todos=file.readlines()
            for index,i in enumerate(todos):
                print(index+1,"-",i.removesuffix("\n"))
            number=int(input("Please enter the no of to do to edit :"))
            with open("todo.txt","r") as file:
                todos=file.readlines()
            todo=input(f"current value of to do is '{todos[number-1]}' Please enter new to do :")+"\n"
            todos[number-1]=todo
            with open("todo.txt","w") as file:
                file.writelines(todos)
        case "complete":
            number=int(input("Please enter the no of to do to complete :"))
            with open("todo.txt","r") as file:
                todos=file.readlines()
            todos.pop(number-1)
            with open("todo.txt","w") as file:
                file.writelines(todos)
        case "completeAll":
            with open("todo.txt","w") as file:
                file.write("")        
        case "exit":
            break    
        case _:
            print("Invalid Input!")    
    