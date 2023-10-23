#To-Do-List
import json
from datetime import datetime
to_do_list =[]
try:
    with open("to_do_list.json", "r", encoding="utf-8") as file:
        content = file.read()
        to_do_list = json.loads(content)
except:
    pass

options = ''' 
(TO-DO-LIST Program)
1-Add a new To-Do item.
2-list your To-Do items.
3-Check status of Task.
4-Search your tasks by title.
5-Change the deadline
6-Exit
'''
print("---Welcome to (TO-DO-LIST) program---")
while True:
    print(options)
    option = input("Choose an option: ")
    if option == "1":
        title =input("Enter the task title: ")
        deadline = input("Enter the deadline:")
        Datetime = datetime.now().strftime("%a, %m-%y %H:%M")
        status ="Not done."
        to_do_list.append({"title": title, "deadline": deadline,"datetime": Datetime,"status":status })
        print("---Added Successfully---")
    elif option == "2":
        for index, elements in enumerate(to_do_list):
            print(f"{index+1}- {elements['title']} - {elements['deadline']} - {elements['datetime']} - {elements["status"]}")
            print("---Operartion Done---")
    elif option == "3":
        for index, elements in enumerate(to_do_list):
            print(f"{index+1}- {elements['title']} - {elements['deadline']} - {elements['datetime']} - {elements["status"]}")
        for index, elements in enumerate(to_do_list):
            num_of_task = int(input("Enter the number of task you have done: "))
            if index+1 ==num_of_task:
                elements['status']='Done.'
                print("---Operartion Done---")
    elif option == "4":
        search_title =input("Type title : ")
        for elements in to_do_list:
            if search_title in elements['title']:
                print(f"{elements['title']} - {elements['deadline']} - {elements['datetime']} - {elements["status"]}")
                print("---Operartion Done---")
    elif option == "5":
        ch_deadline =input("Type a new deadline: ")
        for elements in to_do_list:
            print(f"The old deadline : {elements['title']} - {elements['deadline']} - {elements['datetime']} - {elements["status"]}")       
            elements['deadline']=ch_deadline
            print(f"The new deadline: {elements['title']} - {elements['deadline']} - {elements['datetime']} - {elements["status"]}")
            print("---Operartion Done---")
    elif option == "6":
        with open("to_do_list.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(to_do_list))
            print("Thank you for using the To-Do program, come back again soon")
            break
    else:
        print("Sorry, Invaild input.")
        



