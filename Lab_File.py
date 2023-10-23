while True:
    user=input("Do you want to add a new To-Do item? answer by y for yes and n for no or enter exit to exit the prgram : ")
    if user =="y":
        with open("To-Do.txt","a+",encoding="utf-8") as file:
            writeTxt=input("Enter type in his new To-Do item: ")
            file.write(writeTxt)
    if user=="n":
        userNo=input("do you want to list your To-Do items ? answer y for yes and n for no: ")
        if userNo=="y":
            with open("To-Do.txt", "r", encoding="utf-8") as file:
                content= file.read()
                print(content)
    if user=="exit":
       print("Thank you for using the To-Do program, come back again soon")
       break
    






