# Imports



# Constants

todo_list = ""
todo_dict = {}
todo_items = []


# 

def mainMenu():
    menuHeader = "\n+------- Main Menu -------+"
    menuBody =   "\n| 1) View To Do List      |\n| 2) Add Item             |\n| 3) Remove Item          |\n| 4) Exit                 |"
    menuFooter = "+-------------------------+\n"
    return input(f"{menuHeader}{menuBody}\n{menuFooter}What Would You Like to Do Today?\n> > > ")

def menu(menuTitle, menuContent) -> None:
    menuHeader = f"\n+------- {menuTitle}"
    menuFooter = "+----------------------------------------------------------------+\n"
    print(menuHeader)
    count = 0
    for _ in menuContent:
        print(f"| {menuContent[count]}")
        count+=1
    print(menuFooter)

def getToDoList():
    try:
        with open("todo-list.txt") as raw_todo: # INITIALISATION OF RAW TO-DO
            todo_list = raw_todo.read() # CONVERT: RAW -> LIST
            # VALIDATION : Does To Do List have anything in it?
            if todo_list == "":
                print("Error: No Such To Do List Exists")
                return
            todo_list = todo_list.split("\n") # SPLIT: Individual List Item IF: More Than One Line
    except:
        print("Error: List File Not In Directory")
    count = 0
    for _ in todo_list:
        todo_items.append(f"{count+1} > {todo_list[count]}")
        count+=1
    menu("To Do List", todo_items)
    return count
        
def addToDoListItem():
    task = input("What do you want to add?\n> > > ")
    while task == "":
        task = input("Please enter a valid response!\n> > > ")
    try:
        with open("todo-list.txt","a") as raw_todo: # INITIALISATION OF RAW TO-DO
            raw_todo.write(f"{task}\n")
    except:
        print("Error: List File Not In Directory")
        return
    print("Item Successfully Added")
    getToDoList()

def OverallValidation(value, num):
    try:
        int(value)
        if int(value) in range(0,num):
            _ = "_"
        else:
            raise Exception
    except:
        return True
    return False

def removeToDoListItem():
    lines = getToDoList() + 1 # +1 to allow for the index
    removeWhat = input("What do you want to remove?(use the number)\n> > > ")
    while OverallValidation(removeWhat, lines):
        removeWhat = input("Input a valid number!(use the number)\n> > > ")
    try:
        with open("todo-list.txt","r") as raw_todo: # INITIALISATION OF RAW TO-DO
            todo_list = raw_todo.read() # CONVERT: RAW -> LIST
            # VALIDATION : Does To Do List have anything in it?
            if todo_list == "":
                print("Error: No Such To Do List Exists")
                return
            todo_list = todo_list.split("\n") # SPLIT: Individual List Item IF: More Than One Line
    except:
        print("Error: List File Not In Directory")
    removeItem = int(removeWhat) - 1
    todo_list.pop(removeItem)
    try:
        with open("todo-list.txt","w") as raw_todo: # INITIALISATION OF RAW TO-DO
            for i in todo_list:
                raw_todo.write(f"{i}\n")
    except:
        print("An Error Occurred in removeToDoListItem()")
    todo_items = []
    getToDoList()
    return



# mainMenu()
menuChoice = mainMenu()
# INPUT VALIDATION : main menu choice
while not int(menuChoice) in range(0,5):
    menuChoice = mainMenu()

# IF : check what the user has selected
if int(menuChoice) == 1:
    getToDoList()
elif int(menuChoice) == 2:
    addToDoListItem()
    # raise Exception("Not Implemented") # OLD FROM IMPLEMENTATION
elif int(menuChoice) == 3:
    removeToDoListItem()
    # raise Exception("Not Implemented") # OLD FROM IMPLEMENTATION
elif int(menuChoice) == 4:
    exit()