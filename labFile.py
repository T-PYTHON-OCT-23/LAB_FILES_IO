def toDoList():
    myList = list()
    file = open("to_do.txt","a+", encoding="utf-8")
    print("Welcome to our program!!")
    while True:
        userInput = input("do you want to add a new To-Do item? answer by y for yes and n for no:")

        if userInput == "y":
            userItem = input("Please write new To-Do item:")
            file.write(userItem+"\n")
        elif userInput == "n":
            check = input("do you want to list your To-Do items ? answer y for yes and n for no,write exit to exit.")
            if check == "y":
                file.seek(0)
                myToDo = file.read()
                print(myToDo)
         
            elif check =="exit":
                print("thank you for using the To-Do program, come back again soon")
                file.close()
                break