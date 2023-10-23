
#1 making a program

while True:
    ToDoList = input("do you want to add a new To-Do item? ")
    ToDoList = open("ToDoList.txt", "a",encoding="utf-8" )
    user_answer = input("Your Answer (Y/N)")
    if user_answer == "Y":
        print(input("Type your item in your ToDoList: "))
        user_List = ToDoList.writelines(lines)
        content = ToDoList.readlines()
        print(content + "\n")



    elif user_answer == "N":
        print(input("do you want to list your To-Do items? "))
        if user_answer == "Y":
            ToDoList = open("movie.txt", "r", encoding="utf-8")
            content = ToDoList.read()
            print(content + "\n")
            ToDoList.close()
        if user_answer == "N":
            ToDoList.close()



