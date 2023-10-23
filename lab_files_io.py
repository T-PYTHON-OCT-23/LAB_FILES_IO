while True:
    ask = input("do you want to add a new To-Do item? ('y' for yes and 'n for no ) and if you want exit write 'exit' :\n")
    if ask.lower()=="exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    if ask.lower() == "y":
        to_do = input("What task do you want to add?")
        with open("to_do.txt" ,"a+", encoding="utf-8") as file_to_do:
            file_to_do.write(f"{to_do} \n")
            file_to_do.seek(0)
            read = file_to_do.read()
            print(read)
            
    elif ask.lower() == "n" :
        ask2 = input("do you want to list your To-Do items ? answer 'y' for yes and 'n' for no\n")
        
    if ask2.lower() == "y":
        try:
            with open("to_do.txt" ,"r+" , encoding="utf-8") as for_read :
                print("yout Do list : \n")
                a = for_read.read()
                print(a)
        except FileNotFoundError :
            print("not there your Do list ")
        except Exception as e :
            print(e)
 
            

            


            
            

            
        
    
    