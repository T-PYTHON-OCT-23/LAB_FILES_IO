
print('Welcome to To-Do List Program')


while True:
   ask=input('Do you want to add a new To-Do item? answer by "y" for yes and "n" for no or exist : ')
   if (ask=='y'):
      text=input('Please type in your new To-Do item: ')
      file=open("to_do.txt", "a", encoding="utf-8")
      file.write(text+"\n")
      file.close()
   elif(ask=='n'):
      ask1=input('do you want to list your To-Do items ? answer "y" for yes and "n" for no: ')
      if(ask1=='y'):
         file=open("to_do.txt")
         print(file.read())
         file.close()
   elif(ask=='exist'):
      print('Thank you for using the To-Do program, come back again soon"')
      break
      
      

   
        
        
  
         
            
      
      
   

