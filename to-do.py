while True:
    response = input('Do you want to add a new To-Do item? Answer by "y" for yes and "n" for no. "exit" to exit: ')

    if response == "y":
        new_item = input("Type in your new To-Do item: ")
        with open("to-do.txt", "a", encoding="utf-8") as file:
            file.write(new_item + "\n")

    elif response == "n":
        list_response = input('Do you want to list your To-Do items? Answer "y" for yes and "n" for no: ')

        if list_response == "y":
            with open("to-do.txt", "r", encoding="utf-8") as file:
                list_line_items = file.read()
                print(list_line_items)

    elif response == "exit":
        print("\nThank you for using the To-Do program. Come back again soon.")
   
    else:
        print("Unrecognized input. Please enter 'y' to add, 'n' to list, or 'exit' to exit.")
        break
