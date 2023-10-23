
user_input= input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no " )

while user_input != "exit": 
    if user_input == "y":
     item = input("fill in your to do: ")
     with open ("to_do.txt" , "a" , encoding="utf-8") as file:
      file.write(item + "\n")

    elif user_input =="n":
       list_item = input("do you want to list your To-Do items ?  y or n  ")

       if list_item == "y":
        with open ("to_do.txt" , "r" , encoding="utf-8") as file:
            content = file.read()
            print(content)
         
    elif user_input == "exit":
       break

print("thank you for using the To-Do program, come back again soon" )


     


