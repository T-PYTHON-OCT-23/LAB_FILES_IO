




file = open("to-do.txt")
answer = input ("\n do you want to add a new To-Do item? \n  answer by \"y\" for yes and \"n\" for no ")
while answer != "exit":
    answer = input ("\n do you want to add a new To-Do item? \n  answer by \"y\" for yes and \"n\" for no ")
    print(answer)
    if answer == "y":
        file = open("to-do.txt" , "a" , encoding="utf-8")
        new_item = file.write(input("type in your new To-Do item : " + "\n" )) #in new line
        file.close()
    elif answer == "n":
        answer=(input("do you want to list your To-Do items ? \n answer \"y\" for yes and \"n\" for no."))
        print(answer)
        if answer == "y": #readlines()
            file.seek(0)
            list_lines = file.readlines()
            print(list_lines)
            file.close()
    elif answer == "exit":
        break


print("\n \n thank you for using the To-Do program, come back again soon")
