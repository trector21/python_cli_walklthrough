"""
Work wants an inventory app that:
    Stores Data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            condition 
            ?checkedIn?
"""
# TODO make a menu print out showing options 
def menu():
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete item (By item id)
5. Exit
""")

#List all Items
def list_items():
    for item in items:
        print(ittem)
    print("in list item function")
    pass
#Add New Item 
def new_item():
    global next_id
    name = input("Name: ")
    condition = input("Condtion: ")
    item_id = next_id
    next_id += 1
    pass
#Update Existing Item
def update_existing(itemId):
    pass
#Delete Item (By item Id)
def delete_ittem(itemId):
    pass



# Make the menu questions that grab the data
while True:
    menu()
    choice = (input("> "))

    if choice == "1":
        pass
    elif choice == "2":
        new_item()
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5": #Exit
        exit()
    else:
        input("Invalid Input!\n(Press Enter to try again")
    #Exit
    




# Make the File saving stuff