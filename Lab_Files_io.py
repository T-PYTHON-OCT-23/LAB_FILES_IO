print("********Welcome to To-Do***********")
while True:
    user=input("Do you want to add a new To-Do item? answer by (y) for yes and (n) for no or (exit) to out: ")
    if user.lower() == "exit":
        break 
    if user.lower() == "y":
        items = input("Please type your new To-Do item: ")
        with open("to_do.txt","a+",encoding="utf-8") as file:
            file.writelines(items)

    elif user.lower() == "n":
        user = input("Do you want to list your To-Do items ? answer (y) for yes and (n) for no: ")   
        if user.lower() == "y":
            with open("to_do.txt","r",encoding="utf-8") as file:
                to_do = file.readlines()
                print("This is your To-Do items: ")   
                print(to_do)