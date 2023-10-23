while True: 
 
    response =input("do you want to add a new To-Do item? \n answer by \"y\" for yes  and \"n\" for no: " )
 
    if response == "exit":
      break
    elif response == "y" :
  
       new_item = input("Type in your new To-Do item: ")
       with open("to-do.txt", "a", encoding="utf-8") as file:
            file.write(new_item + '\n')
    elif response == "n":
     
     list_response =input("do you want to list your To-Do items ?  answer by \"y\" for yes and \"n\" for no: " )
    if list_response== "y" :
       with open("to-do.txt", "a", encoding="utf-8")as file:
          list_line_items= file.readline()
          if list_line_items:
           print("Your TO-DO List: ")  
           for i, item in enumerate(list_line_items, 1):
                        print(f"{i}. {item.strip()}")
         # else:
               # print("Your To-Do list is empty.")
    else:
        print("Invalid input. Please enter 'y', 'n', or 'exit'.")
    file.seek(0)     
    file.close()

print("\n Thank you for using the To-Do program. Come back again soon.")

