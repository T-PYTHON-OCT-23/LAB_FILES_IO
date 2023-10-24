import json
from datetime import datetime

def toDoList():
    try:
        with open("to_do.txt", "r", encoding="utf-8") as file:
            content = file.read()
        to_do = json.loads(content)
    except:
        pass
    to_do = []
    usage = '''
    To use the application correctly, please choose the appropriate number for the procedure you want:
    1- Add new To Do to list
    2- Display your To Do list
    3- Search for item in your list
    4- exit

            '''
    file = open("to_do.txt","a+", encoding="utf-8")
    print("Welcome to our program!!")
    while True:
        userInput = input(usage)
        #current_time = datetime.now()
        
        if userInput == "1":
            userItem = input("Please write new To-Do item:")
            myList = {
            "title": userItem,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "done": False
         }
            to_do.append(myList)
            #file.write(json.dumps(myList)+"\n")


        elif userInput == "2":
             for index, todo in enumerate(to_do):
                 mark = ""
                 if todo["done"] == True:
                    mark = "Done"
                 else:
                    mark = "Not Done"
                    output = f"{index+1}- {todo["title"]} - {todo["date_time"] } - {mark}"
                    print(output)
                    isDone = input("Did you do it ? y for yes, n for no: ")
                    if isDone == "y":
                     to_do[index]["done"] = True
            #check = input("do you want to list your To-Do items ? answer y for yes and n for no,write exit to exit.")
        elif userInput == "3":
            userSerach = input("Search for: ")

            foundTitle = [item for item in to_do if userSerach in item["title"]]
            if len(foundTitle) > 0:
                print("Found the following to do:")
                for item in foundTitle:
                    print(f"{item['title']} , {item['date']} - {'Done' if item['done'] else 'Not Done'}")
            else:
                print(f"No results found for {userSerach}")
                
        elif userInput =="4":
                print("thank you for using the To-Do program, come back again soon")
                with open("to_do.txt", "w", encoding="utf-8") as file:
                 content = json.dumps(to_do)
                 file.write(content)



    




toDoList()