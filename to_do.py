
while True:

    user_choice = input('Do you want to add a new To-Do List ? answer by "y" for yes OR "n" for no. "e" to exit :')

    if user_choice.lower() == "y" :
        item = input("Fill in your To Do: ")
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(item + "\n")
    
    elif user_choice.lower() == "n":
        user_input = input('Do you want to list your To-Do items ? answer "y" for yes and "n" for no :')
        if user_input == "y":
            with open("to_do.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
    elif user_choice.lower == "e":
        print("thank you for using the To-Do program, come back again soon!")
        break