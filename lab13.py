#exit= input("If you want to stop write 'Exite' or 'ENTER' to contenuo : ")

while True:
    answer = input("do you want to add a new To-Do item?[answer by 'y' for yes and 'n' for no or 'exit' for exit] ")
    if answer == "y":
#To_Do_iteme = input("Type your new To-Do item :")
        with open ("to_do.txt" , "a" , encoding="utf-8") as file:
            content=input("Type your new To-Do item :")
            file.write(content +"\n")
            print("To-Do item add successfuly")
    elif answer == "n" :
        answer_user2 = input("do you want to list To-Do list?[answer by 'y' for yes and 'n' for no] ")
        if answer_user2 == "y":
            with open ("to_do.txt" , "r" , encoding="utf-8") as file:
                content = file.read()
                print(content)


    elif answer == "exit":
     break
 




