
while True:

    user_choice = input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no. "exit" to exit.')

    if user_choice == "y":
        item = input("Fill in your To Do: ")
        with open("to_do.txt", "a", encoding="utf-8") as file:
            file.write(item + "\n")
    
    elif user_choice == "n":
        user_input = input(' do you want to list your To-Do items ? answer "y" for yes and "n" for no')
        if user_input == "y":
            with open("to_do.txt", "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
    elif user_choice == "exit":
        print("good bye!")
        break