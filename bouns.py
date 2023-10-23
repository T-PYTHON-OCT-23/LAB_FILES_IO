import json

# Function to search for items by keyword
def search_items(data, keyword):
    found_items = []
    for item in data:
        if keyword.lower() in item['TO DO'].lower():
            found_items.append(item)
    return found_items

# Function to change the progress of a To-Do item
def change_progress(data):
    item_index = int(input("Enter the index of the item you want to change progress for: "))
    if 0 <= item_index < len(data):
        new_progress = input("Enter the new progress status (e.g., DONE, IN PROGRESS, NOT DONE): ")
        data[item_index]['TO DO Progress'] = new_progress
        return True
    else:
        print("Invalid item index.")
        return False

while True:
    ans = input("Do you want to add a new To-Do item (y/n), search (s), change progress (c), list (l), or exit (e): ")

    if ans.lower() == "e" or ans.lower() == "exit":
        break
    if ans.lower() == "n" or ans.lower() == "no":
        print("Exiting...")
        break
    if ans.lower() == "l" or ans.lower() == "list":
        print("Listing items:")
        try:
            with open("to_do.json", "r", encoding="UTF-8") as f:
                data = json.load(f)
                for i, item in enumerate(data):
                    print(f"Item {i}:" , end=" ")
                    print(f"TO DO: {item['TO DO']}" , end=" ")
                    print(f"TO DO TIME: {item['TO DO TIME']}"  , end=" ")
                    print(f"TO DO Progress: {item['TO DO Progress']}")
        except:
                print("There is no such file.")
    if ans.lower() == "s" or ans.lower() == "search":
        keyword = input("Enter a keyword to search for items: ")
        with open("to_do.json", "r", encoding="UTF-8") as f:
            data = json.load(f)
            found_items = search_items(data, keyword)
            if found_items:
                print("Found items:")
                for i, found_item in enumerate(found_items):
                    print(f"Item {i}:")
                    print(f"TO DO: {found_item['TO DO']}")
                    print(f"TO DO TIME: {found_item['TO DO TIME']}")
                    print(f"TO DO Progress: {found_item['TO DO Progress']}")
            else:
                print("No matching items found.")
    if ans.lower() == "y" or ans.lower() == "yes":
        try:
            with open("to_do.json", "r", encoding="UTF-8") as f:
                data = json.load(f)
        except:
                data=[]
        new_item = {
                "TO DO": input("Type in To-Do item: "),
                "TO DO TIME": input("Type in Time: "),
                "TO DO Progress": "NOT DONE",
            }
        data.append(new_item)
        with open("to_do.json", "w", encoding="UTF-8") as f:
            json.dump(data, f, indent=4)
    if ans.lower() == "c" or ans.lower() == "change":
        with open("to_do.json", "r+", encoding="UTF-8") as f:
            data = json.load(f)
            if change_progress(data):
                f.seek(0)
                f.truncate()
                json.dump(data, f, indent=4)
