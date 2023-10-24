def main():
    to_do_items = []  

    while True:
        user_input = input("Do you want to add a new To-Do item? (y/n): ").lower()

        if user_input == "y":
            new_item = input(" type in your a new To-Do item ")
            to_do_items.append(new_item)
            with open("to_do.txt", "a") as file:
                file.write(new_item + "\n")
        elif user_input == "n":
            read_input = input("Do you want to list your To-Do items? (y/n): ").lower()
            if read_input == "y":
                print("Your To-Do items:")
                for item in to_do_items:
                    print(item)
            elif read_input == "n":
                exit_input = input("Type 'exit' to exit or press Enter to continue: ")
                if exit_input.lower() == "exit":
                    break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    print("Thank you for using the To-Do program. Come back again soon.")


main()

