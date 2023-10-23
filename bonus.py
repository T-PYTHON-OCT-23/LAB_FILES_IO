import json
from datetime import datetime
to_do_list = []
while True:
    print("Note: to end To-Do Application 'exit'")
    user_input = input("Enter 'y' to write a new To-Do or 'n' to close the To-Do: ")
    if user_input == "y":
        print("___Welcome to out To-Do application_____")
        user_todo_input = input("Enter your To-Do name: ")
        date = str(datetime.now())
        done = input("Write (Done or Not Done): ")
        todo_fomate = {
            "to-do-name":user_todo_input,
            "date": date,
            "done":done
        }
        to_do_list.append(todo_fomate)
    elif user_input == "n":
        no_user_input = input("If do you want to list your To-Do items enter 'y': ")
        if no_user_input == "y":
            try:
                with open("to_do.json", "w") as file:
                    json.dump(to_do_list, file, indent=4)  # Save the To-Do list to a JSON file
                print("To-Do list has been saved to 'to_do.json'")
                for idx, to_do in enumerate(to_do_list, 1):
                    print(f"{idx}. To-Do Name: {to_do['to-do-name']}, Date: {to_do['date']}, State: {to_do['done']}")
            except Exception as e:
                print(e)
    elif user_input == "exit":
        print("thank you for using To-Do program, come back again soon")
        break