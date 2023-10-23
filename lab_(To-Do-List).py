#To-Do-List
print("---Welcome to (TO-DO-LIST) program---")
def to_do_list():
    while True:
        option = input("Do you want to add a new To-Do item? answer by : \n 1-(y) for yes\n 2-(n) for no \n 3-exit.\nChoose an option:")
        if option.lower() == "y":
            print("Your new To-Do-List.")
            file = open('to_do.txt',"a",encoding="utf-8")
            value = input("Type: \n")
            file.writelines(value+"\n")
            file.close()
        elif option.lower() == "n":
            option1 = input("Do you want to list your To-Do items ? \n 1-(y) for yes\n 2-(n) for no \n 3-exit.\nChoose an option:")
            if option1.lower() == "y":
                file = open('to_do.txt',"r",encoding="utf-8")
                file.seek(0)
                content = file.read()
                print(content)
                file.close()
        else:
            if option.lower() == "exit":
                print("Thank you for using the To-Do program, come back again soon")
                break


to_do_list()







