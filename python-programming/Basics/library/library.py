while True:
    lori=input("""
1-Type 'login' for login into application
2-Type 'register' for register as new user          
""")
    match lori:
        case "login":
            with open("lori.txt") as file:
                content=file.readlines()
                content=[i.strip("\n") for i in content]
            if(lori in content):
                activity=input("""
                                1-Type 'show' for available books
                                2-Type 'register' for registring the user
                                3-Type 'login' for login into library 
                                4-Type 'add' for                             
                                """)
        case "register":
            username=input("Enter the username")
            with open()       

    
    