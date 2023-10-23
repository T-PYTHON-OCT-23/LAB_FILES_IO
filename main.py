

while True:
    print("Note: to end To-Do Application 'exit'")
    user_input = input("Enter 'y' to write a new To-Do or 'n' to close the To-Do: ")
    if user_input == "y":
        print("___Welcome to out To-Do application_____")
        user_todo_input = input("Enter your To-Do name: ")
        try:
            with open("to_do.txt", "+a", encoding="utf-8") as file:
                file.write(f"{user_todo_input}\n")
        except Exception as e:
            print(e)
    elif user_input == "n":
        no_user_input = input("If do you want to list your To-Do items enter 'y': ")
        if no_user_input == "y":
            try:
                with open("to_do.txt", "r+", encoding="utf-8") as file:
                    read = file.readlines()
                    for n in read:
                        print(n)
            except Exception as e:
                print(e)
    elif user_input == "exit":
        print("thank you for using To-Do program, come back again soon")
        break