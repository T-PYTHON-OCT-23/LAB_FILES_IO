while True:    
    ans=input("do you want to add a new To-Do item y/n or exit")
    if ans.lower()=="exit":
        break
    if ans.lower()=="n" or ans.lower()=="no":
        ans=input("Do you want to list your items?")
        if ans.lower()=="n" or ans.lower()=="no":
            break
        elif ans.lower()=="y" or ans.lower()=="yes":
            with open("to_do.txt","r",encoding="UTF-8")as f:
                 print(f.readline())
    elif ans.lower()=="y" or ans.lower()=="yes":
        ans=input("type in To-Do item")
        with open("to_do.txt","wt+",encoding="UTF-8") as f: 
             f.write(ans)