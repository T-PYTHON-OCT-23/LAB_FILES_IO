
items=1
while True:

    user_answers=input("do you want to add a new To-Do item? answer by y for yes and n for no and by exit for exit: ")
    if user_answers.lower() == 'y':

        user_writing=input("type in your new To-Do item: ")
        
        with open("to_do.txt","+a",encoding="utf-8") as file:
            file.write(f"{items}-{user_writing}\n")
            items+=1


        
    if user_answers.lower()=='n':
        user_reading=input("do you want to list your To-Do items ? answer y for yes and n for no: ")
        try:
            with open("to_do.txt","r",encoding="utf-8")as file:
                file.seek(0)
                user_items=file.read()
                print(user_items)
        except FileNotFoundError:
            print("sorry file not found")
    if user_answers=="exit":
        print("thank you for using the To-Do program, come back again soon")
        break

        
            

