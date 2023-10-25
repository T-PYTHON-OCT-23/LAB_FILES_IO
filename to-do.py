while True: 
 
  response = input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no. "exit" to exit.')
  if response == "y" :
    new_item = input("Type in your new To-Do item: ")
    with open("to-do.txt", "a", encoding="utf-8") as file:
          file.write(new_item + "\n")
    
  elif response == "n":
     list_response =input(' do you want to list your To-Do items ? answer "y" for yes and "n" for no' )
     if list_response == "y":
       with open("to-do.txt", "r", encoding="utf-8")as file:
         list_line_items= file.read()
         print(list_line_items )
         
  elif list_response =="exit":
      
     print("\n Thank you for using the To-Do program. Come back again soon")
     break
