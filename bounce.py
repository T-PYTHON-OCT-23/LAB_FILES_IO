from datetime import datetime
import json

to_dos = []

try:
    with open("to_do.json", "r", encoding="utf-8") as file:
        content = file.read()
        to_dos = json.loads(content)
except:
    pass


usage = '''
To use Advanced To Do app , choose a number:
1) Add new To Do
2) Display your To Do items
3) Search for an item
4) exit
'''

while True:
    user_choice = input(usage)

    if user_choice == "1":
        new_todo = input("Your To Do: \n")
        item = {
            "title" : new_todo,
            "date" : datetime.now().strftime("%a, %m-%y %H:%M"),
            "done" : False
        }

        to_dos.append(item)
        print("Added item successfully !")
        input("..press Enter to continue")
    elif user_choice == "2":
        for index, item in enumerate(to_dos):
            status = "Done" if item["done"] == True else "Not Done"
            output = f"{index+1}- {item['title']} - {item['date']} - {status}"
            print(output)
            is_done = input("Is this to do done ? y for yes, n for no: ")
            if is_done == "y":
                to_dos[index]["done"] = True
    
    elif user_choice == "3":
        user_serach = input("Search for: ")

        found_results = [item for item in to_dos if user_serach in item["title"]]
        if len(found_results) > 0:
            print("Found the following to do:")
            for item in found_results:
                print(f"{item['title']} , {item['date']} - {'Done' if item['done'] else 'Not Done'}")
        else:
            print(f"No results found for {user_serach}")
        
        input("..press Enter to continue")
    elif user_choice == "4":
        print("Goodbye !!")
        with open("to_do.json", "w", encoding="utf-8") as file:
            content = json.dumps(to_dos)
            file.write(content)

        break