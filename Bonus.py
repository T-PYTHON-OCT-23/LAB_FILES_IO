import json
from datetime import datetime
tasks = []
try:
    with open("to_do.json","r",encoding="utf-8")as file:
        tasks= json.loads(file.read())
except:
    pass
while True:
    user_input=input('\n1. Add a new To-Do task.\n2. Change task status.\n3. Search in task using title\n4. List all tasks\nto exit type "0"\n')
    if user_input=="1":
        title_=input("Title of the new To-Do task: ")
        dateTime_= datetime.now().strftime("%a, %m-%y %H:%M")
        status_="NOT DONE"
        tasks.append({"Title": title_, "dateTime": dateTime_, "status": status_ })
        print("added !")
    elif user_input=="2":
        for index, i in enumerate(tasks):
             print(f"{index+1}- {i['Title']} - {i['dateTime']} - {i["status"]}")
        change_this=input("Enter the number of task you have done: ")
        for index, i in enumerate(tasks):
            if index+1 ==int(change_this):
                i['status']="DONE"

    elif user_input=="4":
        for index, i in enumerate(tasks):
            print(f"{index+1}- {i['Title']} - {i['dateTime']} - {i["status"]}")
    elif user_input=="3":
        search_for=input("Search for (Title of task): ")
        for i in tasks:
            if i['Title']==search_for:
                print(f"{i['Title']} - {i['dateTime']} - {i["status"]}")

    elif user_input=="0":
        print("Bye!")
        with open("to_do.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(tasks))
        break
    else:
        print("Error, please enter a valid input")
        