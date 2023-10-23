while True:
        
    user_input=input('Add a new To-Do item? (answer by "y" for yes and "n" for no.)').lower()
    if user_input=="exit":
        break
    if user_input=="y":
        new_item=input("Please type in the new To-Do item: ")
        with open("to_do.txt","a", encoding="utf-8") as file: 
            file.write(new_item+"\n")
            file.close
    elif user_input=="n":
        user_input=input('List your To-Do items ? (answer "y" for yes and "n" for no.) ').lower()
        if user_input=="y":
            with open("to_do.txt", "r") as file:
                items = file.readlines()
                for i in items:
                    print(i[:-1])
        elif user_input=="n":
            break
    else:
        print("Error, please enter a valid input")
    