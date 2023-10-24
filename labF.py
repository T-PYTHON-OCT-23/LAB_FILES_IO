while True:
    q=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no. or 'exit'")
    if q.lower() == "y":
        i=input(" fill in your data:"" ")
        with open("todo.txt","a", encoding="utf-8") as f:
            f.write(i+"\n")
    elif q =="n":
      q=input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no.")
    elif q =="y":
       with open("todo.txt","r", encoding="utf-8") as f: 
           i=f.read()
           print(i)
    elif q == "exit":
     
        break

  
