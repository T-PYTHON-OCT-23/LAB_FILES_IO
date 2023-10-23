
# 1 making a program

while True:
    ToDoList = input('do you want to add a new To-Do item? click Enter to answer. "exit" to exit.')
    user_answer = input("Your Answer (Y/N): ")
    if user_answer == "Y":
        List = input("Fill in your ToDoList: ")
        with open("ToDoList.txt", "a", encoding="utf-8") as file:
            file.write(List + "\n")
        print(List + "\n")

    elif user_answer == "N":
        user_input = print(input('do you want to list your To-Do items? '))
        if user_input == "Y":
            with open("ToDoList.txt", "r", encoding="utf-8"):
             content = file.read()
             print(content + "\n")
        elif user_answer == "N":
            ToDoList.close()

    elif user_answer == "exit":
        print("Thank you using the To-Do program, come back again soon!")
        break
